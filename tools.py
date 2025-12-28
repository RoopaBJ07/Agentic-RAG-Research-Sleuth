import os
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain_community.tools.semanticscholar.tool import SemanticScholarQueryRun
from langchain_core.tools import tool
from unstructured.partition.pdf import partition_pdf

class AcademicToolkit:
    def __init__(self):
        # Configure ArXiv to allow PDF downloads
        self.arxiv_wrapper = ArxivAPIWrapper(
            top_k_results=3, 
            doc_content_chars_max=1500,
            load_all_available_meta=True
        )

    @tool
    def extract_paper_images(self, arxiv_id: str) -> str:
        """
        Downloads a PDF from ArXiv and extracts all figures, charts, and images.
        Input should be a valid ArXiv ID (e.g., '1706.03762').
        Returns a summary of extracted image paths.
        """
        # 1. Download the PDF
        pdf_path = self.arxiv_wrapper.download_pdf(arxiv_id)
        output_dir = f"./extracted_images/{arxiv_id}"
        os.makedirs(output_dir, exist_ok=True)

        # 2. Partition PDF to find images (using Unstructured)
        # This identifies images and saves them as separate files
        elements = partition_pdf(
            filename=pdf_path,
            extract_images_in_pdf=True,
            infer_table_structure=True,
            chunking_strategy="by_title",
            max_characters=4000,
            new_after_n_chars=3800,
            extract_image_block_output_dir=output_dir,
        )

        return f"Images extracted successfully to {output_dir}. Found {len(elements)} structural elements."

def get_academic_tools():
    toolkit = AcademicToolkit()
    
    # Standard Search Tools
    arxiv_search = ArxivQueryRun(api_wrapper=toolkit.arxiv_wrapper)
    s2_tool = SemanticScholarQueryRun()
    
    # Custom Image Tool
    image_tool = toolkit.extract_paper_images
    
    return [arxiv_search, s2_tool, image_tool]