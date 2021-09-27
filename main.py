from KStockPERGetter import KoreanStockPERSnatcher

import csv

tickers = list()
stocks = open("data_5535_20210926.csv", "r", encoding="cp949")
list_of_stocks = csv.reader(stocks)

for stock in stocks:
    stock_info = stock.split(',')
    stock_ticker = stock_info[0].replace('"','')
    
    tickers.append(stock_ticker)


if __name__ == "__main__":
    for ticker in tickers:
        per_collection = KoreanStockPERSnatcher(ticker)
        stock_soup = per_collection.get_stock_page_parser(ticker)
        per_collection.get_stock_per(stock_soup, ticker)

    print(per_collection.data(ticker))



