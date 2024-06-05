import requests
from bs4 import BeautifulSoup
import pandas as pd
response=requests.get("https://webscraper.io/test-sites/tables")
print(response)
# soup=BeautifulSoup(response.text,"lxml")
# table=soup.find("table" , class_="table table-bordered")
# heading=table.find_all("th")
# heading_list=[]
# for i in heading[1:]:
#     name=i.text
#     heading_list.append(name)
# df=pd.DataFrame(columns=heading_list)
# row=table.find_all("tr")
# print(row)
