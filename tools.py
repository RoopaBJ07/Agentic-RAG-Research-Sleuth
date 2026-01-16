import os
import requests
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain_community.tools.semanticscholar.tool import SemanticScholarQueryRun
from langchain_core.tools import tool
from unstructured.partition.pdf import partition_pdf


@tool
def extract_paper_images(arxiv_id: str) -> str:
    """
    Download a paper PDF from arXiv and extract figures/images.
    """

    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    output_dir = f"./extracted_images/{arxiv_id}"
    os.makedirs(output_dir, exist_ok=True)

    pdf_path = os.path.join(output_dir, f"{arxiv_id}.pdf")

    response = requests.get(pdf_url, timeout=30)
    if response.status_code != 200:
        return f"Failed to download PDF from {pdf_url}"

    with open(pdf_path, "wb") as f:
        f.write(response.content)

    elements = partition_pdf(
        filename=pdf_path,
        extract_images_in_pdf=True,
        extract_image_block_output_dir=output_dir,
    )

    return f"Images extracted to {output_dir}. Found {len(elements)} elements."


def get_academic_tools():
    arxiv_search = ArxivQueryRun(
        api_wrapper=ArxivAPIWrapper(
            top_k_results=3,
            doc_content_chars_max=1500,
            load_all_available_meta=True,
        )
    )

    semantic_scholar_search = SemanticScholarQueryRun()

    return [
        arxiv_search,
        semantic_scholar_search,
        extract_paper_images,
    ]
