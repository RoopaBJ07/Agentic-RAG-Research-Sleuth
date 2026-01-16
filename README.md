# 🎓 Agentic-RAG: Academic Research Detective

## The “Why” Behind the Project  
### A Personal Research Story

This project was born out of a real research bottleneck I encountered during my **M.Tech thesis on Rainfall Forecasting using Machine Learning and Deep Learning**.

During my literature survey, I spent **weeks manually skimming hundreds of research papers** just to find a handful that matched very specific criteria—such as papers using **hybrid neural architectures** (e.g., CNNs for spatial feature extraction combined with LSTMs for temporal modeling).

Generic academic search engines allowed keyword-based searches but failed at:
- filtering by **methodology**
- identifying **model architectures**
- searching by **mathematical formulations**
- understanding **how models were actually constructed**

I realized a large portion of my research time was being wasted on *searching* rather than *thinking*.

---

## The Problem  
### The “Literature Survey Wall”

While working on my thesis, I faced three recurring challenges:

- 🔍 **Methodology Blindness** – Search engines could not retrieve papers based on architectural descriptions or formulas  
- 🧮 **Mathematical Opacity** – Core equations were buried deep inside PDFs and difficult to inspect quickly  
- 📊 **Visual Loss** – Diagrams and figures were inaccessible through text-only RAG systems  

As a result, I spent more time *finding* papers than *learning from* them.

---

## The Solution: Agentic-RAG (Academic Detective)

**Agentic-RAG** is an **agent-driven academic research assistant** designed to transform the traditional *Search → Read → Decide* loop into a **single structured interaction**.

Instead of searching by title alone, researchers can:
- describe a **methodology**
- reference a **formula**
- explain a **problem statement**

…and receive a **structured, research-ready paper profile** in seconds.

---

## Key Features

### 🕵️ Detective Mode (Reverse Lookup)
Search for papers using:
- methodology descriptions  
- neural network architectures  
- mathematical expressions  

instead of relying only on paper titles.

---

### 🧠 Structured Paper Understanding
Automatically generates a **360° academic profile**, including:
- Problem Statement  
- Goal of the Paper  
- Methodology  
- Data Used  
- Key Findings  
- Limitations  

This allows researchers to assess relevance **within seconds**.

---

### ➗ Mathematical Reasoning (Research-Grade)
The system includes a **dedicated math reconstruction module** that:

- Reconstructs **core mathematical formulations** from methodology text  
- Separates **equations and explanations** for clarity  
- Explicitly labels inferred equations to **avoid hallucination**  
- Renders equations cleanly in the UI using LaTeX  

This mirrors how researchers actually interpret papers in practice.

---

### 🧬 Hybrid Architecture Mining
Specifically designed to identify:
- CNN–LSTM hybrids  
- Transformer-based pipelines  
- Multi-model data fusion strategies  

This capability directly reflects the challenges faced during my own thesis work.

---

### 🖼️ Multimodal Vision (When Available)
When possible, the system:
- extracts figures and diagrams from PDFs  
- recovers captions and structural context  

If visual extraction is unreliable, the agent **semantically describes figures** instead of hallucinating images.

---

## Impact: Accelerating the Scholar’s Journey

Research should be about **innovation**, not endless searching.

Agentic-RAG helps by:
- ⏱️ **Reducing literature survey time** by up to ~80% in early stages  
- 📚 Supporting scholars who prefer **primary sources** but face information overload  
- 🔄 Enabling **cross-domain discovery** by matching methodologies across fields  

---

## System Architecture (High-Level)

