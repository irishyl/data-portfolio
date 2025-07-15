# ingest index into ES
import pandas as pd
import json
import requests

ES_URL = "http://localhost:9200"
INDEX  = "retail_products"

# source
df = pd.read_csv("Online Retail.csv")
products = (
    df[["StockCode","Description"]]
      .drop_duplicates("StockCode")
      .dropna(subset=["Description"])
)

# build an NDJSON body for the _bulk API
lines = []
for _, row in products.iterrows():
    # action line
    meta = {"index": {"_index": INDEX, "_id": str(row.StockCode)}}
    lines.append(json.dumps(meta))
    # document source line
    src = {"sku": str(row.StockCode), "description": row.Description}
    lines.append(json.dumps(src))

bulk_body = "\n".join(lines) + "\n"

# send to _bulk endpoint
resp = requests.post(
    f"{ES_URL}/_bulk",
    headers={"Content-Type": "application/x-ndjson"},
    data=bulk_body
)
resp.raise_for_status()
result = resp.json()

# check for errors
if result.get("errors"):
    for item in result["items"][:5]:
        if "error" in item["index"]:
            print("Error indexing:", item["index"]["error"])
    raise RuntimeError("Bulk ingest had errors; see above.")
else:
    print(f"Successfully indexed {len(products)} products.")
