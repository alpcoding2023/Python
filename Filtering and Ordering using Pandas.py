#!/usr/bin/env python
# coding: utf-8

# # Filtering and Ordering

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Pandas\world_population.csv")
df


# In[4]:


# Filter based off of column

df[df['Rank'] < 10]


# In[6]:


# Filter based of specific Value list
specific_entries = ['Bangladesh', 'Brazil']

df[df['Country'].isin(specific_entries)]


# In[7]:


# Contains value
df[df['Country'].str.contains('United')]


# In[9]:


# Filter using index

df2 = df.set_index('Country')
df2 


# In[13]:


# use filter function, & axis (0 is row, 1 - header axis(column)) to filter spefic value as first index

df2.filter(items=['Continent','CCA3'],axis = 1)


# In[14]:



df2.filter(items=['Continent','CCA3'],axis = 1)




# In[15]:


df2.filter(items=['Zimbabwe'],axis = 0)


# In[17]:


# Using like 
df2.filter(like='United',axis = 0)


# In[19]:


# loc and iloc (index location)

df2.loc['United States']

df2.iloc[3]


# In[31]:


# sorting by ORDER By

df[df['Rank'] > 10].sort_values(by='Rank',ascending = False)


# In[30]:





# In[32]:


pd.set_option('display.max.rows',235)
pd.set_option('display.max.columns',50)


# In[36]:


df[df['Rank'] < 10].sort_values(by='Rank',ascending = False)


# In[38]:


# Sort in multiple columns
df[df['Rank'] < 10].sort_values(by=['Continent','Country'],ascending = False)


# In[40]:


df[df['Rank'] < 10].sort_values(by=['Continent','Country'],ascending = [False, True])


# In[ ]:




