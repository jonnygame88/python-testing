
from bs4 import BeautifulSoup
import urllib.request as urlr
import numpy as np
import pandas as pd
pd.set_option('display.width', 1000)

url_match = "http://www.tennisbetsite.com/index.php?option=com_mvx_trdb&Itemid=29&association=A&id1=5992&id2=1075&tid=12811&type=gameinfo"
page_match = urlr.urlopen(url_match)
soup_match = BeautifulSoup(page_match.read(), "lxml")
gs = soup_match.findAll('table', attrs = {'class': 'gamestats'})
print(gs[0].tbody.prettify())
