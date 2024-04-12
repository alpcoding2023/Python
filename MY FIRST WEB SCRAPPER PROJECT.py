#!/usr/bin/env python
# coding: utf-8

# In[61]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[62]:


# for pagination to append later to the extracted hrefs
baseurl = "https://www.motoworld.com.ph"


# In[63]:



# to mimic human requests as much as possible
headers = {
    'User=Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Accept-Language' : 'en-US,en;q=0.9,la;q=0.8',
    'Referer':'https://www.youtube.com/', 
       
}

# to requests html/lxml from website to scrape

#r = requests.get("https://www.motoworld.com.ph/collections/helmets?page=1")
#soup  = BeautifulSoup(r.content, "lxml")


# to extract all of the product listed on one page

#productlist = soup.find_all('div', class_="card__info-inner inline-block w-full")

#productlinks = []

# looping through the a tags from the extracted card or product listed on the page

#for card in productlist:
  #  for link in card.find_all('a', href = True):
        #print(link['href'])
       # productlinks.append(baseurl + link['href'] )


#print(len(productlinks))

# to loop through all pagitation, we need to creat a for loop 1-26 as it is 25 pages
# use the url of the 1st page as initial request as a f string to increment the number of the pages

productlinks = []

for x in range(1,26):
    
    r = requests.get(f"https://www.motoworld.com.ph/collections/helmets?page={x}")
    soup  = BeautifulSoup(r.content, "lxml")

    productlist = soup.find_all('product-card', class_="card card--product h-full card--product-contained card--no-lines relative flex")
    
  
    for card in productlist:
        for link in card.find_all('a', href = True):
            productlinks.append(baseurl + link['href'] )

#print(productlinks)

# To get product information we'll have to loop through each links (like clicking on to each products) and exact the data

#testlink = "https://www.motoworld.com.ph/collections/helmets/products/ff320-evo-mara-full-face-helmet"

#r = requests.get(testlink, headers = headers)

#soup = BeautifulSoup(r.content, "lxml")

#name = soup.find('h1', class_="product-title h5").text.strip()
#ratings = soup.find('span', class_="wc_product_review_avg_badge_countr")
#reviews = soup.find('span', class_="wc_product_review_text")
#price = soup.find('strong', class_="price__current").text.strip()
#print(name, ratings, reviews, price)

#helmet = {
#    'name' : name,
#    'ratings' : ratings,
#    'reviews' : reviews,
#    'price' : price
#}




# In[66]:


helmet_list = []

for link in productlinks:
    
    r = requests.get(link, headers = headers)

    soup = BeautifulSoup(r.content, "lxml")

    name = soup.find('h1', class_="product-title h5").text.strip()
    price = soup.find('strong', class_="price__current").text.strip()
    try:
        ratings = soup.find('span', class_="wc_product_review_avg_badge_count").text.strip()
    except:
        rating = 'No Rating'
    try:
        reviews = soup.find('span', class_="wc_product_review_text").text.strip()
    except:
        riviews = 'No Reviews'
    
    #print(name, ratings, reviews, price)

    helmet = {
        'name' : name,
        'price' : price,
        'ratings' : ratings,
        'reviews' : reviews
        
    }
    
    helmet_list.append(helmet)
    print("Saving...!", helmet['name'])
    

# saving to pandas dataframe

df = pd.DataFrame(helmet_list)
print(df.head(20))


# In[ ]:




