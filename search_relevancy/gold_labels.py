import pandas as pd


df = pd.read_csv("candidates_with_descriptions.csv")
gold_df = df[df["is_gold"] == 1]

GOLD = (
    gold_df
      .groupby("query")["sku"]
      .apply(lambda skus: list(map(str, skus)))
      .to_dict()
)


print(GOLD)
