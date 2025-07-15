# retail_rag.py

import os
import openai
from whoosh import index
from whoosh.qparser import QueryParser
from textwrap import dedent

# 1) Configure your API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # or set it here directly

# 2) Open Whoosh index
ix   = index.open_dir("retail_index")
qp   = QueryParser("content", ix.schema)

def retrieve(query, topn=5):
    """Return list of (sku, description) for top-N hits."""
    with ix.searcher() as s:
        q      = qp.parse(query)
        hits   = s.search(q, limit=topn)
        return [(hit["sku"], hit["content"]) for hit in hits]

def recommend(query):
    """RAG: retrieve top docs, then ask the LLM to recommend."""
    docs = retrieve(query)
    # Build a bullet-list of items
    items_text = "\n".join(
        f"- SKU {sku}: {desc[:100].strip()}…"
        for sku, desc in docs
    )
    prompt = dedent(f"""
        You are a helpful product recommendation assistant.
        A user wants: "{query}"
        Here are the top candidate products with their short descriptions:
        {items_text}

        Please pick the 3 most relevant products and, for each, give a one-sentence reason why
        it fits the user's need. Format your answer as:
        1. SKU <sku> — <reason>
        2. SKU <sku> — <reason>
        3. SKU <sku> — <reason>
    """).strip()

    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"You recommend retail products based on descriptions."},
            {"role":"user",  "content":prompt}
        ],
        temperature=0.7,
        max_tokens=200
    )
    return resp.choices[0].message.content.strip()

if __name__=="__main__":
    user_q = input("Search & Recommend for: ")
    print("\n🔎 Retrieving top products…")
    for sku,desc in retrieve(user_q):
        print(f"{sku} → {desc[:60]}…")
    print("\n💡 LLM Recommendation:\n")
    print(recommend(user_q))
