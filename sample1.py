import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")
product_name=soup.find_all("a",class_="title")
product_name_list=[]
for i in product_name:
    product=i.text
    product_name_list.append(product)
print(product_name_list)


