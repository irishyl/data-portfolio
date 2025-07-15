import streamlit as st
import pandas as pd
import textwrap

# --- Configuration ---
PAGE_TITLE = "🔬 Search Relevance Evaluation"
CLIENT = "Personal Project"
ROLE = "Data Scientist"
YEAR = "2025"
TECH_STACK = ["Python", "Whoosh (TF-IDF)", "Elasticsearch (BM25)", "Docker", "Streamlit"]
OBJECTIVE = (
    "This project was motivated by the need to demonstrate how search quality directly impacts user satisfaction and business outcomes in an e-commerce context. By benchmarking a lightweight TF‑IDF prototype against a robust BM25 engine, we gain insights into ranking effectiveness and practical trade‑offs between rapid prototyping and production‑grade solutions.  "
)

# --- Load Data ---
summary = pd.read_csv("search_relevancy/4_metrics_summary.csv")


# --- Streamlit Layout ---
st.set_page_config(page_title=PAGE_TITLE, layout="wide")
st.title(PAGE_TITLE)

## Project Overview
st.subheader("Project Overview")
st.markdown(f"**Client:** {CLIENT}  ")
st.markdown(f"**Role:** {ROLE}  ")
st.markdown(f"**Year:** {YEAR}  ")
st.markdown(
    "**Data Source:** "
    "[UCI Online Retail Dataset]"
    "(https://archive.ics.uci.edu/dataset/352/online+retail)"
)
st.markdown(f"**Technology Stack:** {', '.join(TECH_STACK)}")
st.markdown("")


## Objective
st.subheader("Objective")
st.markdown(OBJECTIVE)
st.markdown("")

## Methodology
st.subheader("Methodology")
st.markdown("- **Schema & Indexing**: Used Whoosh for a quick TF-IDF prototype; deployed Elasticsearch via Docker for BM25.")
st.markdown("- **Test Set**: Curated 10 real-world queries and hand-labeled 3–5 relevant SKUs each.")
st.markdown("- **Metrics Computation**: Calculated P@10, R@10, nDCG@10, and MRR using Python scripts against both engines.")
st.markdown("")


## Evaluation Results
st.subheader("Average Retrieval Metrics")
st.markdown("- The table below summarizes the performance of the two search engines over our curated 20-query test set.")
st.markdown("- Metrics include Precision@10, Recall@10, nDCG@10, and Mean Reciprocal Rank (MRR).")

st.table(summary)

col1, col2 = st.columns(2)
with col1:
    st.markdown("##### Precision@10 & Recall@10")
    st.bar_chart(summary[["P@10","R@10"]])
    st.markdown(
        "- **Precision@10** measures the proportion of relevant results in the top 10."
        "- **Recall@10** measures the proportion of all relevant items retrieved in the top 10."
    )
with col2:
    st.markdown("##### nDCG@10 & MRR")
    st.line_chart(summary[["nDCG@10","RR"]])
    st.markdown(
        "- **nDCG@10** accounts for both relevance and ranking position."
        "- **Mean Reciprocal Rank (MRR)** captures how soon the first relevant item appears."
    )

st.markdown("")

## Key Insights
st.subheader("Key Insights")
st.markdown("1. **Elasticsearch (BM25)** achieved a Precision@10 of ~0.66 vs. Whoosh’s ~0.49, indicating more relevant items in the top results.")
st.markdown("2. Recall@10 improved from 0.40 (TF-IDF) to 0.60 (BM25), showing better coverage of relevant products.")
st.markdown("3. nDCG@10 rose from 0.65 to 0.82, reflecting stronger ranking quality under BM25.")
st.markdown("4. MRR of 1.0 for Elasticsearch means every first result was relevant, compared to 0.86 for Whoosh.")



