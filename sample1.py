import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/tables"
response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")
product_name=soup.find_all("a",class_="title")
product_name_list=[]
for i in product_name:
    product=i.text
    product_name_list.append(product)

price=soup.find_all("h4", class_="price float-end card-title pull-right")
price_list=[]
for i in price:
    name=i.text
    price_list.append(name)

description=soup.find_all("p", class_="description card-text")
description_list=[]
for i in description:
    name=i.text
    description_list.append(name)
print(description_list)

table=soup.find("table" , class_="table table-bordered")
headers=table.find_all("th")
header=[]
for i in headers:
    name=i.text
    header.append(name)
df=pd.DataFrame(columns=header)

row=table.findAll("tr")
for i in row[1:]:
    data=i.find_all("td")
    row=[tr.text for tr in data]
    l=len(df)
    df.loc[l]=row
print(df)
# df.to_csv("test table.csv")
# add new line



