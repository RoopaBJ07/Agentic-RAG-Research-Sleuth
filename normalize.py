def build_paper_details(raw_paper: dict) -> PaperDetails:
    return PaperDetails(
        title=raw_paper.get("title", "Unknown Title"),

        authors=[
            author.get("name", "")
            for author in raw_paper.get("authors", [])
            if isinstance(author, dict)
        ],

        publication_year=raw_paper.get("year"),
        arxiv_id=raw_paper.get("externalIds", {}).get("ArXiv", "N/A"),
        code_repository=raw_paper.get("code", None),

        abstract=raw_paper.get("abstract", ""),

        problem_statement="Automatically extracted by agent",
        goal_of_the_paper="Automatically extracted by agent",

        methodology="Extracted via agent reasoning",
        data_used="Referenced in paper",

        findings="Derived from results section",
        conclusion="Derived from conclusion section",

        limitations=None,
        references=[],
        figures=[],

        match_confidence=0.8
    )
