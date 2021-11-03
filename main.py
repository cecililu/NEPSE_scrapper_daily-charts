import requests
from bs4 import BeautifulSoup
import pandas
#gettin base url
url="http://www.nepalstock.com/main/todays_price/index/7/"
#gettin the html
response=requests.get(url)
html=response.content
#filtering all tr as they contain individual stocks 
soup=BeautifulSoup(html,'html.parser') 
tr_of_each_stock=[]
for i in range(2,22):
  tr_of_each_stock.append(soup.find_all("tr")[i])
# print(tr_of_each_stock)
#making a list of dictionery  and each stock has one sictionary
#
# 
#  
print("\n \n ___________________________________________________")
alist=[]

print(tr_of_each_stock[0].contents)
for  i in tr_of_each_stock:
    newd={}
    newd['name']=i.contents[3].string
    newd['no of trans']=i.contents[5].string
    newd['max price']=i.contents[7].string
    newd['min price']=i.contents[9].string
    newd['Closing price']=i.contents[11].string
    newd['Traded shares']=i.contents[13].string
    
    newd['amount']=i.contents[15].string
    newd['Prev closing']=i.contents[17].string
    newd['difference']=float(i.contents[11].string)-float(i.contents[17].string)
    alist.append(newd)

print(pandas.DataFrame(alist))