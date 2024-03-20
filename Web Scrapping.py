#!/usr/bin/env python
# coding: utf-8

# 

# # Importing HTML - using BeautifulSoup & Requests

# In[13]:



from bs4 import BeautifulSoup
import requests


url = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(url)

# <Response [200]> -- good request

soup = BeautifulSoup(page.text, 'html')

print(soup.prettify)


# # Find and Find All

# In[16]:


from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(url)

soul = BeautifulSoup(page.text, 'html')
print(soul.prettify)


# In[17]:


soup.find('div')
# find = will only find 1st responds


# In[19]:


soup.find_all('div', class_='col-md-12')
#find_all = will return all 


# In[21]:


soup.find_all('p',class_="lead")


# In[23]:


soup.find('p',class_="lead").text.strip()


# In[28]:


soup.find('th').text.strip()


# # Scrapping Data from Real Website + Pandas
# 

# In[141]:


from bs4 import BeautifulSoup  # import bs4 (to import BeautifulSoup module) library
import requests        # import requests function from BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue' # indicate url 

page = requests.get(url) #call requests get function

soup = BeautifulSoup(page.text, 'html') #pull html from website(url) as text, assign in to a variable (soup)

# extract table you wish to pull using find all (pull up 2nd table ) as text and use strip to clean


table= soup.find_all('table')[1]

#extract table headers (th) and use for to append to a list 

worlds_titles = table.find_all('th')

worlds_table_titles = [titles.text.strip() for titles in worlds_titles ]


# import pandas to save data to data frame and assign data from to df as variable to save table header list

import pandas as pd

df = pd.DataFrame(columns= worlds_table_titles)

# loop through all table rows to scrape data from table data (td) and append to a list

column_row = table.find_all('tr')


# spicify begining arg of list due to empty row []
for row in column_row[1:] :
    column_data_row = row.find_all('td')
    individual_row_data = [data.text.strip() for data in column_data_row]
    
    # to place each row to its appropriate columns of dataframe, 
    #identify the lenght (len) df and use .loc to identify corresponding row
    #looping through row data and appending the values to the df
    
    length = len(df)
    df.loc[length] = individual_row_data 
    
df


# In[136]:





# In[142]:


# export as csv & exclude index

df.to_csv(r'C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Python\Web Scrapping\USA_Top_Companies.csv',index = False)


# In[ ]:





# In[ ]:




