import datetime
import requests
from bs4 import BeautifulSoup as BS

ticker = "039020"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}
url = f"https://finance.naver.com/item/main.naver?code={ticker}"
res = requests.get(url, headers=headers)
soup = BS(res.text, features="html.parser")

ind_stock = soup.select(".wrap_company > h2 > a")[0].text
per = soup.select("#_per")[0].text
result = {"ticker": ticker, "ind_stock": ind_stock, "per": per}

print(result)
