import requests
from bs4 import BeautifulSoup
import pandas as pd
from ai import speak,audio
name=audio()
url=requests.get('https://www.google.com/search?q''='+str(name)+'+share+price')

soup = BeautifulSoup(url.text,'lxml')

a=soup.select('div',class_="BNeawe iBp4i AP7Wnd")[105].getText()

h=(a).replace("Disclaimer","").replace("Stock Price","stock price is  ").replace("/","")
print(h)

