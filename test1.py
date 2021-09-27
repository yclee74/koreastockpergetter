import csv

tickers = list()
stocks = open("data_5535_20210926.csv", "r", encoding="cp949")
list_of_stocks = csv.reader(stocks)

for stock in stocks:
    stock_info = stock.split(',')
    stock_ticker = stock_info[0].replace('"','')
    
    tickers.append(stock_ticker)

print(tickers)


