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
 'limit':'50',
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


# In[12]:


df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')
df


# In[7]:


# Automate process to append data to data frame
import pandas as pd

def api_runner():
    
    global df
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'50',
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
    
    
    
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')
    #df
    
    if not os.path.isfile(r'C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Python\API\Crytpo_API.csv'):
        df.to_csv(r"C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Python\API\Crytpo_API.csv", header='column_names')
    else:
        #append if already exist
        df.to_csv(r'C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Python\API\Crytpo_API.csv', mode= 'a', header=False)



# In[8]:


import os
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print("API Runner completed successfully!")
    sleep(60) # sleep for 1 minute
exit()


# In[11]:


df8 = pd.read_csv(r'C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Python\API\Crytpo_API.csv')    
df8
#pd.set_option('display.max_columns',None) 


# In[13]:





# In[14]:


#display float format with 5 dicemals for large numbers with scientific notation
pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[16]:


df8


# In[55]:


# grouping all price upadate by name by average price change
df_groupby = df8.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df_groupby


# In[56]:


dfToCSV = df_groupby.to_csv(r"C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Python\API\Crytpo_Grouped.csv", header='column_names')
dfRead = pd.read_csv(r'C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Python\API\Crytpo_Grouped.csv')
dfRead


# In[57]:


# for vizualization on the updates, columns must be row, to do that we can stack them

dfStacked = df_groupby.stack()
dfStacked


# In[23]:


type(dfStacked)


# In[58]:


#But since it's not changed to series no longer a data frame, 
# We need to change it back to as dataframe

dfReFrame = dfStacked.to_frame(name='values')
dfReFrame


# In[26]:


type(dfReFrame)


# In[59]:


#However name acts as index but we won't be able to call the index
# One way to index it is to set pd index equal to the range count 
# Then reset the index
dfReFrame.count()


# In[60]:


index = pd.Index(range(300))


# In[61]:


dfIndexed = dfReFrame.reset_index()
dfIndexed


# In[62]:


dfIndexed = dfReFrame.reset_index()
dfIndexed


# In[79]:


# rename the column as it shows level_1
dfRenamed = dfIndexed.rename(columns={'level_1' : 'change_percentage'})
dfRenamed


# In[64]:


dfRenamedToCSV = dfRenamed.to_csv(r"C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Python\API\Crytpo_ChangeRate.csv", header='column_names')
dfRead1 = pd.read_csv(r'C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Python\API\Crytpo_ChangeRate.csv')
dfRead1


# In[74]:


# Vizualation
# import seaborn and matploblib

import seaborn as sns
import matplotlib.pyplot as plt


# In[75]:


#creating x,y legend
sns.catplot(x='change_percentage', y='values', hue = 'name', data = dfRenamed, kind = 'point')


# In[82]:


# to have a better x axis value we can replace the change_percentage name to shorter version


dfRenamed['change_percentage'] = dfRenamed['change_percentage'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1hr','24hr','7d','30d','60d','90d'])
dfRenamed


# In[83]:



sns.catplot(x='change_percentage', y='values', hue = 'name', data =dfRenamed, kind = 'point')


# In[84]:


# to get a more specific values, we can indicate the columns and query the name of cryto you want to pull

dfRenamed= df[['name','quote.USD.price','timestamp']]
dfCrypto = dfRenamed.query("name == 'Bitcoin'")
dfCrypto


# In[85]:


sns.lineplot(x='timestamp',y='qoute.USD.price', data = dfRenamed)


# In[ ]:




