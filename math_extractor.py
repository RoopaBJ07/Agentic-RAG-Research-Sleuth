print("math_extractor module START")

from langchain_openai import ChatOpenAI

print("imports done")

MATH_PROMPT = """
You are analyzing an academic research paper.
TEXT:
{context}
"""

def extract_and_summarize_math(context: str) -> str:
    print("extract_and_summarize_math CALLED")

    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0
    )

    response = llm.invoke(
        MATH_PROMPT.format(context=context)
    )

    return response.content

print("math_extractor module END")
