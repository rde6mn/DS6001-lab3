# %%
import numpy as np
import pandas as pd
import requests
import json
import os
import dotenv

# %% [markdown]
# ## Load API keys secretly as env  variables

# %%
dotenv.load_dotenv()
newskey = os.getenv("newskey")
congresskey = os.getenv("congresskey")

# %%
useragent = 'python-requests/2.32.4'

# %%
headers = {'User-Agent': useragent,
           'From': 'rde6mn@virginia.edu'}
headers['User-Agent'] = 'rde6mn/0.0 (rde6mn@virginia.edu) python-requests/2.32.4'

# %%
params = {'apiKey': newskey,
          'q': '"john mcguire"'}

# %%
root = 'https://newsapi.org'
endpoint = '/v2/everything'
r = requests.get(root + endpoint, headers=headers, params=params)

# %%
r

# %%
newsdf = pd.json_normalize(r.json(), record_path=['articles'])

# %%
newsdf

# %% [markdown]
# ## Congress API

# %%

root = 'https://api.congress.gov/v3'

# %%
stateCode = 'VA'
district = '5'

# %%
endpoint = f'member/{stateCode}/{district}'
root + endpoint

# %%
params = {'format': 'json',
          'currentMember': 'True'
          'api_key': congresskey}

# %%
r = requests.get(root + endpoint, headers=headers, params=params)
r

# %%
bioguideId = r.json()['members'][0]['bioguideId']

# %%
endpoint = f'/member/{bioguideId}/sponsored-legislation'
params = {'api_key': congresskey,
          'format': 'json',
          'offset': 0,
          'limit': 250}

r = requests.get(root + endpoint, headers=headers, params=params)

# %%
r.json()


