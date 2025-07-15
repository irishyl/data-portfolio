import math
import pandas as pd
from gold_labels import GOLD
from es_vs_whoosh import whoosh_top10, es_top10 

def dcg_at_k(preds, gold, K):
    dcg = 0.0
    for i, p in enumerate(preds[:K], start=1):
        rel = 1 if p in gold else 0
        dcg += (2**rel - 1) / math.log2(i+1)
    return dcg

def idcg_at_k(gold, K):
    ideal = min(len(gold), K)
    return sum((2**1 - 1) / math.log2(i+1) for i in range(1, ideal+1))

def ndcg_at_k(preds, gold, K): # Normalized Discounted Cumulative Gain
    idcg = idcg_at_k(gold, K)
    return dcg_at_k(preds, gold, K) / idcg if idcg > 0 else 0.0

def reciprocal_rank(preds, gold):
    for i, p in enumerate(preds, start=1):
        if p in gold:
            return 1 / i
    return 0.0

results = []
K = 10
for q, gold in GOLD.items():
    # Whoosh: get just the SKUs
    w_hits = whoosh_top10(q)
    w_preds = [sku for sku, _ in w_hits]
    
    # ES: similarly extract SKUs
    e_hits = es_top10(q)
    e_preds = [sku for sku, _ in e_hits]

    for engine, preds in [("Whoosh", w_preds), ("Elasticsearch", e_preds)]:
        results.append({
            "Engine": engine,
            "Query":  q,
            f"P@{K}": len([p for p in preds[:K] if p in gold]) / K,
            f"R@{K}": len([p for p in preds[:K] if p in gold]) / len(gold),
            f"nDCG@{K}": ndcg_at_k(preds, gold, K),
            "RR":    reciprocal_rank(preds, gold)
        })

df = pd.DataFrame(results)
# Now group by Engine and average the metrics
summary = df.groupby("Engine")[[f"P@{K}", f"R@{K}", f"nDCG@{K}", "RR"]].mean()
print(summary)
