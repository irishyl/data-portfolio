from es_vs_whoosh import whoosh_top10, es_top10
import csv
import pandas as pd

products_df = pd.read_csv("Online Retail.csv")[["StockCode","Description"]]
products_df = (
    products_df
    .drop_duplicates("StockCode")
    .rename(columns={"StockCode":"sku"})
)


QUERIES = [
    "coffee mug",
    "gift wrap paper",
    "cordless drill under 50",
    "stainless steel bowl",
    "led outdoor floodlight",
    "tea spoon", 
    "coat rack", 
    "chalkboard", 
    "wall clock",
    "red pen"
]


candidates = {}
for q in QUERIES:
    candidates[q] = {
      "whoosh": whoosh_top10(q),
      "es":     es_top10(q)
    }

rows = []
for query, engines in candidates.items():
    for engine_name, hits in engines.items():
        for rank, (sku, score) in enumerate(hits, start=1):
            rows.append({
                "query":   query,
                "engine":  engine_name,
                "rank":    rank,
                "sku":     sku,
                "score":   score
            })

cand_df = pd.DataFrame(rows)

merged = cand_df.merge(products_df, on="sku", how="left")
merged.to_csv("candidates_with_descriptions.csv", index=False)
