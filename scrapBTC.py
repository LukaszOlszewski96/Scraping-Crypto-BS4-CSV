import datetime
import time
import csv
from bs4 import BeautifulSoup
from requests import get

#scraping data from website


def readPriceBTC():
        URL = 'https://www.coingecko.com/en'
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        resultsBTC = bs.find('table', {'class' : 'table-scrollable'}).find('tbody').find_all('tr')
        date_read = datetime.date.today()
        time_read = datetime.datetime.now().strftime('%H:%M:%S')
        name = resultsBTC[0].find('a', {'class' : 'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip()
        price = resultsBTC[0].find('td', {'class' : 'td-price price text-right'}).get_text().strip()
        volume_24h = resultsBTC[0].find('td', {'class' : 'td-liquidity_score lit text-right %> col-market'}).get_text().strip()
        mkt_cap = resultsBTC[0].find('td', {'class' : 'td-market_cap cap col-market cap-price text-right'}).get_text().strip()
        return [
        date_read,
        time_read,
        name,
        price,
        volume_24h,
        mkt_cap,
        print(date_read,time_read,name,price,volume_24h,mkt_cap)
        ]

#Csv file
FILENAME_BTC = 'historical_BTC.csv'

with open(FILENAME_BTC, 'a', newline="") as file:
    csvWriter = csv.writer(file)
    while True:
        csvWriter.writerow(readPriceBTC())
        time.sleep(1)

