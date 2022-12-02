from lxml import etree
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from tqdm import tqdm, trange
import warnings
warnings.filterwarnings("ignore")
dfAll = pd.DataFrame()

listTitle=[]
listUrl=[]
All_list=[]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}
for  i in trange(10000,14069):
	url="https://www.linetv.tw/drama/"+str(i)
	res=requests.get(url)
	soup=BeautifulSoup(res.text,'lxml')
	title=soup.title.text
	print(title)
	print(url)
	if "線上看" in title:
		dfAll=dfAll.append({"Platform":"line_TV","Title":title,"URL":url}, ignore_index=True)
		dfAll.drop_duplicates(subset='URL',inplace=True)
		print("OK")
	print("-------")
print(dfAll.to_json())
dfAll.to_csv("./LineTV_All.csv", encoding = 'utf-8',index = True)