import os
from dotenv import load_dotenv
from functools import lru_cache

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor,create_openai_tools_agent

# Project imports
from schemas import PaperDetails
from tools import get_academic_tools
from prompts import get_academic_prompt
from math_extractor import extract_and_summarize_math


# Load environment variables
load_dotenv()


def _init_agent():
    """
    Initialize and cache the agent + LLM.
    This prevents re-creation on every Streamlit rerun.
    """

    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0
    )

    tools = get_academic_tools()
    prompt = get_academic_prompt()

    agent = create_openai_tools_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True
    )

    return agent_executor, llm
def is_math_heavy(text: str) -> bool:
    keywords = [
        "loss", "objective", "optimization", "probability",
        "likelihood", "softmax", "embedding", "gradient",
        "neural", "model", "representation", "equation"
    ]
    return any(k in text.lower() for k in keywords)


def run_academic_agent(user_query: str) -> PaperDetails:
    """
    Runs the agentic academic research pipeline and
    ALWAYS returns a validated PaperDetails object.
    """

    agent_executor, llm = _init_agent()

    print(f"\n--- Processing Query: {user_query} ---")

    # 1. Agent reasoning + tool usage
    raw_response = agent_executor.invoke(
        {"input": user_query}
    )

    reasoning_text = raw_response["output"]

    # 2. Decide whether math is required
    user_wants_math = "math" in user_query.lower() or "formula" in user_query.lower()

    force_math = any(
        key in reasoning_text.lower()
        for key in ["attention", "transformer", "residual"]
    )

    if is_math_heavy(reasoning_text) or force_math or user_wants_math:
        math_summary = extract_and_summarize_math(reasoning_text)
    else:
        math_summary = "No explicit mathematical formulation detected."

    # 3. Enforce structured output (math INCLUDED in content)
    structured_llm = llm.with_structured_output(PaperDetails)

    final_output = structured_llm.invoke(
        f"""
        Convert the following content into a structured academic paper profile.
        If information is missing, infer conservatively and do NOT hallucinate.

        CONTENT:
        {reasoning_text}

        MATHEMATICAL BASIS:
        {math_summary}
        """
    )

    return PaperDetails.model_validate(final_output)


# -------------------------------
# Local test (NOT used by Streamlit)
# -------------------------------
if __name__ == "__main__":
    query = (
        "Find the paper that introduced Residual Connections "
        "and uses the formula y = F(x) + x"
    )

    result = run_academic_agent(query)

    print("\n--- FINAL STRUCTURED OUTPUT ---")
    print(result.model_dump_json(indent=2))
