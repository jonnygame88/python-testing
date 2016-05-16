
from bs4 import BeautifulSoup
import urllib.request as urlr
import numpy as np
import pandas as pd
pd.set_option('display.width', 1000)

## get match urls
url_player = "http://www.tennisbetsite.com/players/atp/novak-djokovic.html"
page_player = urlr.urlopen(url_player)
soup_player = BeautifulSoup(page_player.read(), "lxml")
match_links = []
for link in soup_player.find_all('a'):
    link_url = link.get('href')
    if "gameinfo" in link_url and link_url not in match_links:
        match_links.append(link_url)

## get match stats
def match_stats(n):
    url_match = match_links[n]
    page_match = urlr.urlopen(url_match)
    soup_match = BeautifulSoup(page_match.read(), "lxml")
    gs = soup_match.findAll('table', attrs = {'class': 'gamestats'})[0].tbody
    gs_title = gs.findAll(attrs = {'class': 'title'})
    gs_val = gs.findAll(attrs = {'class': 'value'})
    t_metrics = [i.get_text() for i in gs_title]
    t_vals = [i.get_text() for i in gs_val]
    t_entries = [[t_metrics[i], t_vals[2*i], t_vals[2*i + 1]] for i in range(14)]
    return(pd.DataFrame(t_entries, columns = ['metric', 'player1', 'player2']))

for n in range(len(match_links)):
    print(match_stats(n))
    print("\n")
