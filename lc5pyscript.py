# %%
import numpy as np
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup

# %%
useragent = f'ds6001rt/0.0 (rde6mn@virginia.edu) python-requests/{requests.__version__}'
useragent

# %%
headers = {'User-Agent': useragent, 'From': 'rde6mn@virginia.edu'}

# %%
url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:a_z?page=5'

# %%
r = requests.get(url, headers=headers)
r

# %%
mysoup = BeautifulSoup(r.text, 'html.parser')


# %%
ataglist = mysoup.find_all('a', attrs={'data-track':'scores'})

# %%
ataglist[20]['href']

# %%
urllist = ['https://www.rottentomatoes.com' + m['href'] for m in ataglist]

# %%
url = urllist[0]

# %%
url

# %%
r = requests.get(url, headers=headers)
r

# %%
mysoup = BeautifulSoup(r.text, 'html.parser')

# %%
mysoup.find_all('rt-text', attrs={'slot':'criticsScore', 'role': 'button'})[0].text


