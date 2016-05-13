
from bs4 import BeautifulSoup
import urllib.request
import numpy as np
import pandas as pd
pd.set_option('display.width', 1000)

## get monthly urls
url_main = "http://www.valuehorsetips.co.uk/purchase-subscription/"
page_main = urllib.request.urlopen(url_main)
soup_main = BeautifulSoup(page_main.read(), "lxml")
month_links = []
for link in soup_main.find_all('a'):
    link_url = link.get('href')
    if "record" in link_url or "result" in link_url:
        month_links.append(link.get('href'))

## get monthly results
for i in range(1, 25):
    url_month = month_links[len(month_links) - i]
    page_month = urllib.request.urlopen(url_month)
    soup_month = BeautifulSoup(page_month.read(), "lxml")
    bets_raw = soup_month.div.table.get_text()
    bets = ' '.join(bets_raw.replace('\n\n', ' ').replace('\n', ';').replace('NR', '0').split()).split(';')
    col_names = [i.replace(' ', '') for i in bets[0:7]]
    bets = pd.DataFrame([bets[i:(i + 7)] for i in range(7, len(bets), 7) if '/' in bets[i + 1]])
    bets.columns = col_names
    print(url_month, len(bets.Profit), pd.DataFrame.sum(pd.to_numeric(bets.Profit)))
