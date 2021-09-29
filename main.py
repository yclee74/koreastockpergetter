import csv

from tqdm import tqdm

from kstock_per_getter import KoreanStockPERSnatcher

if __name__ == "__main__":
    file = open("data_5535_20210926.csv", "r", encoding="cp949")
    reader = csv.reader(file)

    per_collection = KoreanStockPERSnatcher()

    with open("result.csv", "w") as res_file:
        writer = csv.writer(res_file)
        for stock in tqdm(list(reader)):
            ticker = stock[0]
            data = per_collection.get_per(ticker)
            writer.writerows([list(data.values())])
