import datetime
import requests
from bs4 import BeautifulSoup as BS


class KoreanStockPERSnatcher:
    def __init__(self):

        date = datetime.datetime.today()
        self.date = date.strftime("%Y%m%d")

    def get_per(self, ticker):

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/39.0.2171.95 Safari/537.36"
        }
        url = f"https://finance.naver.com/item/main.naver?code={ticker}"
        res = requests.get(url, headers=headers)
        soup = BS(res.text, features="html.parser")

        ind_stock = soup.select(".wrap_company > h2 > a")[0].text
        if soup.select("#_per"):
            per = soup.select("#_per")[0].text
        else:
            per = "NA"

        return {
            "ticker": ticker,
            "ind_stock": ind_stock,
            "date": self.date,
            "per": per,
        }
