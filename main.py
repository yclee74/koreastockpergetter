import csv

from tqdm import tqdm
import pandas as pd

from kstock_per_getter import KoreanStockPERSnatcher

if __name__ == "__main__":
    file = open("data_5535_20210926.csv", "r", encoding="cp949")
    reader = csv.reader(file)

    per_collection = KoreanStockPERSnatcher()
    for stock in tqdm(list(reader)):
        ticker = stock[0]
        per_collection.get_per(ticker)

    df = pd.DataFrame(per_collection.data)
    df.T.to_csv("result.csv")
