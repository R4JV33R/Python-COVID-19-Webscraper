import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/coronavirus/country/india/"


#for n in names: 
  #  print(n,names[n])
   # search_url = (url + n[0] + "/"+names[n]+".html")
    #print (n.split(" "))


 #   myList = n.list[0:5]

print(search_url)
search_page = requests.get(search_url, headers=headers)
print (search_page)