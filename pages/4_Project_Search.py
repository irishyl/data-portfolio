import streamlit as st
import pandas as pd

# --- Configuration ---
PAGE_TITLE = "🔬 Search Engine Evaluation"
CLIENT = "Personal Project"
ROLE = "Data Scientist"
YEAR = "2025"
DATA_SOURCE = "UCI Online Retail Dataset (∼4,000 products)"
TECH_STACK = ["Python", "Whoosh (TF-IDF)", "Elasticsearch (BM25)", "Docker", "Streamlit"]
OBJECTIVE = (
    "This project was motivated by the need to demonstrate how search quality directly impacts user satisfaction and business outcomes in an e-commerce context. By benchmarking a lightweight TF‑IDF prototype against a robust BM25 engine, we gain insights into ranking effectiveness and practical trade‑offs between rapid prototyping and production‑grade solutions.  "
)

# --- Load Data ---
# summary = pd.read_csv("search_relevancy/metrics_summary.csv")
# print(summary.head)


# --- Streamlit Layout ---
st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)

## Project Overview
st.markdown(f"**Client:** {CLIENT}  ")
st.markdown(f"**Role:** {ROLE}  ")
st.markdown(f"**Year:** {YEAR}  ")
st.markdown(f"**Data Source:** {DATA_SOURCE}  ")
st.markdown(f"**Objective:** {OBJECTIVE}")
st.markdown(f"**Technology Stack:** {', '.join(TECH_STACK)}")

st.markdown("---")

## Methodology
st.markdown(
    "- **Schema & Indexing**: Used Whoosh for a quick TF-IDF prototype; deployed Elasticsearch via Docker for BM25."
    "- **Test Set**: Curated 10 real-world queries and hand-labeled 3–5 relevant SKUs each."
    "- **Metrics Computation**: Calculated P@10, R@10, nDCG@10, and MRR using Python scripts against both engines."
)

st.markdown("---")

## Evaluation Results
st.subheader("Average Retrieval Metrics")
st.markdown(
    "The table below summarizes the performance of the two search engines over our curated 20-query test set. "
    "Metrics include Precision@10, Recall@10, nDCG@10, and Mean Reciprocal Rank (MRR)."
)
# st.table(summary)

# col1, col2 = st.columns(2)
# with col1:
#     st.subheader("Precision@10 & Recall@10")
#     st.bar_chart(summary[["P@10","R@10"]])
#     st.markdown(
#         "- **Precision@10** measures the proportion of relevant results in the top 10."
#         "- **Recall@10** measures the proportion of all relevant items retrieved in the top 10."
#     )
# with col2:
#     st.subheader("nDCG@10 & MRR")
#     st.line_chart(summary[["nDCG@10","RR"]])
#     st.markdown(
#         "- **nDCG@10** accounts for both relevance and ranking position."
#         "- **Mean Reciprocal Rank (MRR)** captures how soon the first relevant item appears."
#     )

st.markdown("---")

## Key Insights
st.markdown(
    "1. **Elasticsearch (BM25)** achieved a Precision@10 of ~0.66 vs. Whoosh’s ~0.49, indicating more relevant items in the top results."
    "2. Recall@10 improved from 0.40 (TF-IDF) to 0.60 (BM25), showing better coverage of relevant products."
    "3. nDCG@10 rose from 0.65 to 0.82, reflecting stronger ranking quality under BM25."
    "4. MRR of 1.0 for Elasticsearch means every first result was relevant, compared to 0.86 for Whoosh."
)


