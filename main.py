import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent

# Import our modular components
from schemas import PaperDetails
from tools import get_academic_tools
from prompts import get_academic_prompt

# Load Environment Variables (API Keys)
load_dotenv() 

def run_academic_agent(user_query: str):
    #  Initialize the LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # Load our custom toolkit
    tools = get_academic_tools()

    # Initialize the Brain (Prompt)
    prompt = get_academic_prompt()

    # Build the Agent
    agent = create_openai_tools_agent(llm, tools, prompt)

    # 6. Initialize the Executor
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True, 
        handle_parsing_errors=True
    )

    # Execute and Force Structured Output
    print(f"--- Processing Query: {user_query} ---")
    
    raw_response = agent_executor.invoke({"input": user_query})
    structured_llm = llm.with_structured_output(PaperDetails)
    final_output = structured_llm.invoke(raw_response["output"])
    
    return final_output

# --- EXAMPLE USAGE ---
if __name__ == "__main__":
    # Test Case 1: Title Search
    # result = run_academic_agent("Find the details for the paper 'Attention is All You Need'")
    
    # Test Case 2: Reverse Lookup (The "Detective" Feature)
    query = "Find the paper that introduced Residual Connections and uses the formula y = F(x) + x"
    result = run_academic_agent(query)
    
    print("\n--- FINAL STRUCTURED DATA ---")
    print(result.model_dump_json(indent=2))