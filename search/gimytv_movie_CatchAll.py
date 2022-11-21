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
for  i in trange(652):
	response = requests.get(
		"https://gimytv.tv/genre/movies---"+str(i)+".html", headers=headers)
	soup = BeautifulSoup(response.text, "html.parser")
	#print(soup.prettify())
	result = soup.find("ul", class_="myui-vodlist clearfix")
	#print(result)
	titles=result.find_all("a",class_="myui-vodlist__thumb lazyload")
	#print(titles)
	#urls=result.find_all("a", class_="theme-list-main")
	for A in titles:
		title=A['title']
		url="https://gimytv.tv"+A['href']
		print(title)
		print(url)
		dfAll=dfAll.append({"Platform":"gimytv","Title":title,"URL":url}, ignore_index=True)
		dfAll.drop_duplicates(subset='URL',inplace=True)
		print("----")
dfAll.to_csv("./GimyTV_Movie.csv", encoding = 'utf-8',index = True)