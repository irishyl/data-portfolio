import pandas as pd
from whoosh import index
from whoosh.fields import Schema, ID, TEXT
import os
import pandas as pd

# define schema
schema = Schema(
    sku=ID(stored=True, unique=True),
    content=TEXT(stored=True) 
)

# create/open index
if not os.path.exists("retail_index"):
    os.mkdir("retail_index")
    ix = index.create_in("retail_index", schema)
else:
    ix = index.open_dir("retail_index")

# load products
df = pd.read_csv("Online Retail.csv")

products = (
  df[["StockCode", "Description"]]
  .drop_duplicates(subset="StockCode")
  .dropna(subset=["Description"])
  .reset_index(drop=True)
)
# print(products.head)

# write index
writer = ix.writer()
for _, row in products.iterrows():
    writer.update_document(
        sku=str(row.StockCode),
        content=row.Description
    )
writer.commit()
print("Indexed", len(products), "products")



'''checking '''
# ix = index.open_dir("retail_index")

# # print out one to check
# with ix.searcher() as searcher:
#     for docnum in searcher.reader().all_doc_ids():
#         fields = searcher.stored_fields(docnum)
#         print(f"Doc {docnum}: {fields}")
#         break
