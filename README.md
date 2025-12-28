**The "Why" Behind the Project:**
***A Personal Research Story:***
This project was born out of a real-world bottleneck I encountered during my M.Tech research in Rainfall Forecasting using Deep Learning. 
***The Problem:***
 The "Literature Survey" Wall While working on my thesis, I found myself spending weeks performing literature surveys. I had to sift through hundreds of papers manually just to find the "needle in the haystack"—papers that specifically used Hybrid Neural Network architectures (like combining CNNs for spatial data with LSTMs for temporal sequences).
Generic search engines couldn't filter by specific Methodologies, Data Fusion techniques, or LaTeX formulas. I realized I was wasting valuable research time on administrative skimming rather than actual innovation.
***The Solution: Agentic-RAG:***
I built this "Academic Detective" to protect my time and the time of every other scholar. It transforms the "Search-to-Learning" ratio by allowing researchers to search for problem-specific papers and get instant, structured insights into how others solved similar technical challenges.


**Key Features:**
Detective Mode: Perform "Reverse Lookups" using methodology descriptions or formulas instead of just titles.
Structural Extraction: Automatically populates a 360° profile (Problem Statement, Goal, Methodology, Findings) so you can decide if a paper is relevant in seconds.
Hybrid Architecture Mining: Specifically designed to find how researchers integrate multiple models (CNN, LSTM, Transformer) and handle niche data preprocessing.
Multimodal Vision: Recovers diagrams, charts, and captions directly from PDFs to provide visual context that text-only RAG misses.


**Impact: Accelerating the Scholar's Journey**
Research should be about innovation, not searching. Agentic-RAG democratizes deep research by:
Eliminating "Wasted Time": Reduces initial literature review time by up to 80%.
Supporting Complex Learning: Helps scholars who, like me, prefer learning from primary sources but struggle with information overload.
Cross-Domain Discovery: Helps find methodologies from other fields that can be applied to your specific problem statement.


**Tech Stack:**
Orchestration: LangChain (OpenAI Tools Agent)
LLM: GPT-4o (Reasoning & Vision)
Data Sources: ArXiv API, Semantic Scholar API
Parsing: unstructured.io (PDF-to-Image & OCR)
Validation: Pydantic V2 (Structured Output)
UI: Streamlit


**System Architecture:**
The agent follows a multi-stage Reasoning Loop:
Intent Analysis: Determines if the user is looking for a specific paper or exploring a methodology.
Tool Selection: Dynamically queries ArXiv or Semantic Scholar.
Deep Extraction: Downloads the PDF and uses Vision-LLMs to "read" the methodology and extract figures.
Verification: Ensures the extracted data matches the high-fidelity Pydantic schema before display.


**Getting Started:**
1. Prerequisites
Python 3.10+
System Tools: poppler-utils and tesseract-ocr (for PDF processing).
2. Installation
Bash
git clone https://github.com/YOUR_USERNAME/Agentic-RAG.git
cd Agentic-RAG
pip install -r requirements.txt
3. Environment Setup
Create a .env file:
Plaintext
OPENAI_API_KEY=your_key_here
SEMANTIC_SCHOLAR_API_KEY=your_key_here  # Optional for higher rate limits
4. Run the App
Bash
streamlit run app.py


**Technical Challenges Solved:**
PDF Layout Analysis: Overcoming multi-column scientific formats to extract clean text.
Rate-Limit Management: Implementation of Exponential Backoff to respect non-profit API infrastructures.
Hallucination Control: Using strict Pydantic validation to ensure extracted methodologies are grounded in the paper text.

