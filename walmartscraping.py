from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random


productNames = []
productDesc = []

start = 1
end = 5

# Food Products
urls = [f"https://www.walmart.com/search/?cat_id=976759&page={i}&query=" for i in range(start,end)]
for url in urls:
    page = requests.get(url)
    soup = bs(page.content, features="lxml")
    for i in soup.find_all(class_='product-title-link line-clamp line-clamp-2 truncate-title'):
        temppage = i.get('href')
        newpage = "https://walmart.com" + temppage
        productpage = requests.get(newpage)
        soup2 = bs(productpage.content, features='lxml')
        for d in soup2.find_all(class_='about-desc about-product-description xs-margin-top'):
            if d.text != None:
                for n in soup2.find_all(class_='prod-ProductTitle prod-productTitle-buyBox font-bold'):
                    productNames.append(n.text)
                    productDesc.append(d.text)

# Electronic Products
urls = [f"https://www.walmart.com/search/?cat_id=3944&page={i}&query=" for i in range(start,end)]
for url in urls:
    page = requests.get(url)
    soup = bs(page.content, features="lxml")
    for i in soup.find_all(class_='product-title-link line-clamp line-clamp-2 truncate-title'):
        temppage = i.get('href')
        newpage = "https://walmart.com" + temppage
        productpage = requests.get(newpage)
        soup2 = bs(productpage.content, features='lxml')
        for d in soup2.find_all(class_='about-desc about-product-description xs-margin-top'):
            if d.text != None:
                for n in soup2.find_all(class_='prod-ProductTitle prod-productTitle-buyBox font-bold'):
                    productNames.append(n.text)
                    productDesc.append(d.text)

# Toys Products
urls = [f"https://www.walmart.com/search/?cat_id=4171&page={i}&query=" for i in range(start,end)]
for url in urls:
    page = requests.get(url)
    soup = bs(page.content, features="lxml")
    for i in soup.find_all(class_='product-title-link line-clamp line-clamp-2 truncate-title'):
        temppage = i.get('href')
        newpage = "https://walmart.com" + temppage
        productpage = requests.get(newpage)
        soup2 = bs(productpage.content, features='lxml')
        for d in soup2.find_all(class_='about-desc about-product-description xs-margin-top'):
            if d.text != None:
                for n in soup2.find_all(class_='prod-ProductTitle prod-productTitle-buyBox font-bold'):
                    productNames.append(n.text)
                    productDesc.append(d.text)

# Home Products
urls = [f"https://www.walmart.com/search/?cat_id=4044&page={i}&query=" for i in range(start,end)]
for url in urls:
    page = requests.get(url)
    soup = bs(page.content, features="lxml")
    for i in soup.find_all(class_='product-title-link line-clamp line-clamp-2 truncate-title'):
        temppage = i.get('href')
        newpage = "https://walmart.com" + temppage
        productpage = requests.get(newpage)
        soup2 = bs(productpage.content, features='lxml')
        for d in soup2.find_all(class_='about-desc about-product-description xs-margin-top'):
            if d.text != None:
                for n in soup2.find_all(class_='prod-ProductTitle prod-productTitle-buyBox font-bold'):
                    productNames.append(n.text)
                    productDesc.append(d.text)

# Health Products
urls = [f"https://www.walmart.com/search/?cat_id=976760&page={i}&query=" for i in range(start,end)]
for url in urls:
    page = requests.get(url)
    soup = bs(page.content, features="lxml")
    for i in soup.find_all(class_='product-title-link line-clamp line-clamp-2 truncate-title'):
        temppage = i.get('href')
        newpage = "https://walmart.com" + temppage
        productpage = requests.get(newpage)
        soup2 = bs(productpage.content, features='lxml')
        for d in soup2.find_all(class_='about-desc about-product-description xs-margin-top'):
            if d.text != None:
                for n in soup2.find_all(class_='prod-ProductTitle prod-productTitle-buyBox font-bold'):
                    productNames.append(n.text)
                    productDesc.append(d.text)

# Music Products
urls = [f"https://www.walmart.com/search/?cat_id=4104&page={i}&query=" for i in range(start,end)]
for url in urls:
    page = requests.get(url)
    soup = bs(page.content, features="lxml")
    for i in soup.find_all(class_='product-title-link line-clamp line-clamp-2 truncate-title'):
        temppage = i.get('href')
        newpage = "https://walmart.com" + temppage
        productpage = requests.get(newpage)
        soup2 = bs(productpage.content, features='lxml')
        for d in soup2.find_all(class_='about-desc about-product-description xs-margin-top'):
            if d.text != None:
                for n in soup2.find_all(class_='prod-ProductTitle prod-productTitle-buyBox font-bold'):
                    productNames.append(n.text)
                    productDesc.append(d.text)

# Pet Products
urls = [f"https://www.walmart.com/search/?cat_id=5440&page={i}&query=" for i in range(start,end)]
for url in urls:
    page = requests.get(url)
    soup = bs(page.content, features="lxml")
    for i in soup.find_all(class_='product-title-link line-clamp line-clamp-2 truncate-title'):
        temppage = i.get('href')
        newpage = "https://walmart.com" + temppage
        productpage = requests.get(newpage)
        soup2 = bs(productpage.content, features='lxml')
        for d in soup2.find_all(class_='about-desc about-product-description xs-margin-top'):
            if d.text != None:
                for n in soup2.find_all(class_='prod-ProductTitle prod-productTitle-buyBox font-bold'):
                    productNames.append(n.text)
                    productDesc.append(d.text)

# Video Game Products
urls = [f"https://www.walmart.com/search/?cat_id=2636&page={i}&query=" for i in range(start,end)]
for url in urls:
    page = requests.get(url)
    soup = bs(page.content, features="lxml")
    for i in soup.find_all(class_='product-title-link line-clamp line-clamp-2 truncate-title'):
        temppage = i.get('href')
        newpage = "https://walmart.com" + temppage
        productpage = requests.get(newpage)
        soup2 = bs(productpage.content, features='lxml')
        for d in soup2.find_all(class_='about-desc about-product-description xs-margin-top'):
            if d.text != None:
                for n in soup2.find_all(class_='prod-ProductTitle prod-productTitle-buyBox font-bold'):
                    productNames.append(n.text)
                    productDesc.append(d.text)

# Patio and Garden Products
urls = [f"https://www.walmart.com/search/?cat_id=5428&page={i}&query=" for i in range(start,end)]
for url in urls:
    page = requests.get(url)
    soup = bs(page.content, features="lxml")
    for i in soup.find_all(class_='product-title-link line-clamp line-clamp-2 truncate-title'):
        temppage = i.get('href')
        newpage = "https://walmart.com" + temppage
        productpage = requests.get(newpage)
        soup2 = bs(productpage.content, features='lxml')
        for d in soup2.find_all(class_='about-desc about-product-description xs-margin-top'):
            if d.text != None:
                for n in soup2.find_all(class_='prod-ProductTitle prod-productTitle-buyBox font-bold'):
                    productNames.append(n.text)
                    productDesc.append(d.text)

df = pd.DataFrame()
df['Product Name'] = productNames
df['Product Descriptions'] = productDesc
df.to_csv('walmartscrapes.csv')

###########################################################################################################################################################################################################

url = 'https://td2020-static.s3.amazonaws.com/glove.6B.50d.txt'
r = requests.get(url)
open('glove.6B.50d.txt', 'wb').write(r.content)

from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = 'glove.6B.50d.txt'
word2vec_output_file = 'glove.6B.50d.txt.word2vec'
glove2word2vec(glove_input_file, word2vec_output_file)
from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)

def clean(desc):
    # remove stop words (the, a)
    # lematizing
    # stemming
    desc = ''.join([char if str.isalpha(char) else ' ' for char in desc.lower()]).split()
    return [word for word in desc if word in model.wv.vocab]

def search(query, productDesc):
    sim = lambda desc1, desc2: model.n_similarity(clean(desc1), clean(desc2))
    return np.argmax([sim(query, desc) for desc in productDesc])


query = input("Enter search query: ")
if query:
    match_idx = search(query, productDesc)
    print('Matched Product for ' + query + ':', productNames[match_idx])
    tempNames = productNames
    tempDesc = productDesc
    del tempNames[match_idx]
    del tempDesc[match_idx]
    print('Similar Product:', tempNames[search(productDesc[match_idx], tempDesc)])