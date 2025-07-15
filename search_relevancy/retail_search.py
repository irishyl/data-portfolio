from whoosh import index, scoring
from whoosh.qparser import QueryParser

ix = index.open_dir("retail_index")


def search(q, topn=5):
    with ix.searcher() as s:
        parser = QueryParser("content", ix.schema)
        q = parser.parse(q)
        results = s.search(q, limit=topn)
        for hit in results:
            print(f"{hit['sku']}:{hit['content']}: {hit.score:.2f}")



if __name__ == "__main__":
    query = input("Search term: ")
    search(query)

