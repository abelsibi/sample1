import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://ticker.finology.in/"
response_html=requests.get(url)
soup=BeautifulSoup(response_html.text,"lxml")
table1=soup.find("table" , class_="table table-sm table-hover screenertable")
headers=table1.find_all("th")
header_list=[]
for i in headers:
    name=i.text
    header_list.append(name)
df=pd.DataFrame(columns=header_list)
row=table1.find_all("tr")
for i in row[1:]:
    data=i.find_all("td")
    row=[tr.text for tr in data]
    l=len(df)
    df.loc[l]=row
df.to_csv("stockmarket price.csv")