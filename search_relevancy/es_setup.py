import requests

ES_URL = "http://localhost:9200"
INDEX  = "retail_products"

# delete the index if it exists (ignore 404)
resp = requests.delete(f"{ES_URL}/{INDEX}")
if resp.status_code not in (200, 404):
    raise RuntimeError(f"Unexpected DELETE status: {resp.status_code} {resp.text}")

# create the index with BM25 mapping
mapping = {
  "mappings": {
    "properties": {
      "sku":         {"type": "keyword"},
      "description": {"type": "text",    "analyzer": "standard"}
    }
  }
}
resp = requests.put(f"{ES_URL}/{INDEX}", json=mapping)
resp.raise_for_status()

print(f"Index `{INDEX}` ready (was deleted if it existed).")
