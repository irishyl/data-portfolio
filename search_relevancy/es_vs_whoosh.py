from whoosh import index as windex
from whoosh.qparser import QueryParser
import requests

# whoosh
w_ix = windex.open_dir("retail_index")
w_qp = QueryParser("content", w_ix.schema)

# ES
ES_URL = "http://localhost:9200"
INDEX  = "retail_products"

def whoosh_top10(q):
    with w_ix.searcher() as s:
        qobj = w_qp.parse(q)
        hits = s.search(qobj, limit=10)
        return [(hit["sku"], hit.score) for hit in hits]

def es_top10(q):
    body = {
        "size": 10,
        "query": {
            "match": {"description": q}
        }
    }
    resp = requests.get(
        f"{ES_URL}/{INDEX}/_search",
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        json=body
    )
    resp.raise_for_status()
    hits = resp.json()["hits"]["hits"]
    return [(h["_source"]["sku"], h["_score"]) for h in hits]

if __name__ == "__main__":
    TEST_QUERIES = [
        "coffee mug",
        "gift wrap",
        "cordless drill under 50",
        "chocolate box",
        "stainless steel bowl"
    ]
    for q in TEST_QUERIES:
        print(f"\n=== Query: “{q}” ===")
        print("Whoosh (TF-IDF):      ", whoosh_top10(q))
        print("Elasticsearch (BM25): ", es_top10(q))
