from pydantic import BaseModel, Field
from typing import List, Optional

class ReferencePaper(BaseModel):
    """Schema for individual papers cited within the main research paper."""
    title: str = Field(..., description="The title of the referenced research paper")
    relevance: Optional[str] = Field(None, description="Why this paper was cited (e.g., 'Used for baseline comparison' or 'Foundation for the loss function')")

class FigureData(BaseModel):
    """Schema for extracting visual data and diagrams mentioned in the paper."""
    figure_label: str = Field(..., description="The label of the figure, e.g., 'Figure 1'")
    caption: str = Field(..., description="The full caption describing what is shown in the image or chart")
    image_path: Optional[str] = Field(None, description="Local file path or URL to the extracted image file")

class PaperDetails(BaseModel):
    """The complete analytical profile of a research paper for automated extraction."""
    
    # --- 1. Identification & Metadata ---
    title: str = Field(..., description="The full official title of the research paper")
    authors: List[str] = Field(default_factory=list, description="A clean list of all authors")
    publication_year: Optional[int] = Field(None, description="The year the paper was published")
    arxiv_id: str = Field(..., description="The unique ArXiv identifier (e.g., '1706.03762')")
    code_repository: Optional[str] = Field(None, description="The GitHub or official code link if mentioned")

    # --- 2. Narrative & Structure ---
    abstract: str = Field(..., description="The complete abstract of the paper")
    problem_statement: str = Field(..., description="The specific problem or research gap the paper addresses")
    goal_of_the_paper: str = Field(..., description="The primary objective or hypothesis of this research")
    introduction_summary: Optional[str] = Field(None, description="Summary of the context and background provided in the introduction")

    # --- 3. Technical Implementation ---
    methodology: str = Field(..., description="Detailed description of the proposed architecture, algorithm, or research design")
    mathematical_basis: Optional[str] = Field(None, description="Key mathematical formulas or concepts in LaTeX format (e.g., $L = \text{softmax}(x)$)")
    data_used: str = Field(..., description="Specific datasets, benchmarks, or data sources used")

    # --- 4. Outcomes & Conclusions ---
    findings: str = Field(..., description="The core results, performance metrics achieved, or discoveries")
    conclusion: str = Field(..., description="The final takeaways and suggested future work")
    limitations: Optional[str] = Field(None, description="Constraints or weaknesses acknowledged by the authors")

    # --- 5. Relational & Multimodal Data ---
    references: List[ReferencePaper] = Field(default_factory=list, description="List of key papers cited in this research")
    figures: List[FigureData] = Field(default_factory=list, description="List of figures, captions, and their corresponding extracted paths")

    # --- 6. Verification ---
    match_confidence: float = Field(..., description="Confidence score (0.0 to 1.0) indicating how well this matches the user's initial query")