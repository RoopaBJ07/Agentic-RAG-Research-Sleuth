import streamlit as st
import json
from main import run_academic_agent

# 1. Page Configuration
st.set_page_config(page_title="AI Academic Detective", page_icon="🎓", layout="wide")

st.title("🎓 Academic Research Agent")
st.markdown("Search for papers by **Title** or describe a **Methodology/Formula** to find its source.")

# 2. Sidebar for Status & Settings
with st.sidebar:
    st.header("Settings")
    st.info("Agent is using GPT-4o + ArXiv + Semantic Scholar")
    if st.button("Clear Cache"):
        st.cache_data.clear()

# 3. User Input
query = st.text_input("Enter Paper Title or Description (e.g., 'The paper that introduced Transformers'):")

if query:
    with st.spinner("🕵️ Agent is researching... this may take a minute for PDF/Image processing."):
        try:
            # Call your main agent function
            result = run_academic_agent(query)
            print(type(result))
            
            # 4. Display Results in Columns
            col1, col2 = st.columns([2, 1])

            with col1:
                st.header(result.title if hasattr(result, "title") else result.get("title", "Unknown Title"))
                authors = ", ".join(result.authors) if result.authors else "Not extracted"
                year = result.publication_year if result.publication_year else "Year unknown"
                st.subheader(f"Authors: {authors} ({year})")
                
                st.markdown("### 📝 Abstract")
                st.write(result.abstract)
                
                st.markdown("### 🔬 Methodology")
                st.info(result.methodology)
                
                st.markdown("### 🔢 Mathematical Basis")
                math_text = result.mathematical_basis

                if math_text and "EQUATIONS:" in math_text:
                    equations, explanation = math_text.split("EXPLANATION:", 1)

                    equations = equations.replace("EQUATIONS:", "").strip()
                    explanation = explanation.strip()

                    if equations:
                        st.latex(equations)

                    if explanation:
                        st.markdown("**Explanation**")
                        st.write(explanation)
                else:
                    st.write("No explicit mathematical formulation detected.")


            with col2:
                st.markdown("### 🎯 Problem & Goal")
                st.success(f"**Problem:** {result.problem_statement}")
                st.success(f"**Goal:** {result.goal_of_the_paper}")
                
                st.markdown("### 📊 Key Findings")
                st.warning(result.findings)

            # 5. Display Images if they exist
            if result.figures:
                st.divider()
                st.header("🖼️ Extracted Figures")
                img_cols = st.columns(len(result.figures))
                for i, fig in enumerate(result.figures):
                    with img_cols[i]:
                        if fig.image_path:
                            st.image(fig.image_path, caption=fig.caption)
                        else:
                            st.caption(f"**{fig.figure_label}**: {fig.caption}")

            # 6. References
            st.divider()
            with st.expander("📚 Key References"):
                for ref in result.references:
                    st.write(f"- **{ref.title}**: {ref.relevance}")

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.divider()
st.caption("M.Tech Interview Project | Built with LangChain, Pydantic, and Streamlit")