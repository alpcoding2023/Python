#!/usr/bin/env python
# coding: utf-8

# In[1]:



#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
 'start':'1',
 'limit':'5000',
 'convert':'USD'
}
headers = {
 'Accepts': 'application/json',
 'X-CMC_PRO_API_KEY': '74dce221-3713-4911-8e34-c90f76566e26',
}

session = Session()
session.headers.update(headers)

try:
 response = session.get(url, params=parameters)
 data = json.loads(response.text)
 print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
 print(e)
 


# In[2]:


type(data)


# In[3]:


import pandas as pd


# In[7]:




pd.set_option('display.max_columns',None)


# In[8]:


pd.json_normalize(data['data'])


# In[ ]:




