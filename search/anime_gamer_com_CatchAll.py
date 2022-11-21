import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import warnings
warnings.filterwarnings("ignore")
dfAll = pd.DataFrame()

listTitle=[]
listUrl=[]
All_list=[]
keyword="搖曳露營"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}
for  i in range(50):
    response = requests.get(
        "https://ani.gamer.com.tw/animeList.php?page="+str(i)+"&c=All&sort=1", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup.prettify())
    result = soup.find("div", class_="theme-list-block")
    titles=result.find_all("p",class_="theme-name")
    urls=result.find_all("a", class_="theme-list-main")
    list_dict = dict()
    for title in titles:
        listTitle.append(title.text)
        list_dict['title'] = title.text
        #print(title.text)
    for url in urls:
        listUrl.append(url.get("href"))
        list_dict['url']=url.get("href")
        #print(url.get("href"))
    #print(listTitle)
    #print(listUrl)
    for i in range(0,len(listTitle)):
        title=listTitle[i]
        url="https://ani.gamer.com.tw/"+listUrl[i]
        dfAll=dfAll.append({"Platform":"anime_gamer","Title":title,"URL":url}, ignore_index=True)
        dfAll.drop_duplicates(subset='URL',inplace=True)
print(dfAll.to_json())
dfAll.to_csv("./AnimeGamer.csv", encoding = 'utf-8',index = True)
'''#print(soup.prettify())  #輸出排版後的HTML內容
result = soup.find("div", class_="theme-list-block")
titles=result.find_all("p",class_="theme-name")
urls=result.find_all("a", class_="theme-list-main")
#print(urls)
for title in titles:
    listTitle.append(title.text)
    #print(title.text)
for url in urls:
    listUrl.append(url.get("href"))
    #print(url.get("href"))
for i in range(0,len(listTitle)):
    TagsList=[]
    title=listTitle[i]
    TagsList.append(keyword)
    TagsList.append(title)
    jsonArr = json.dumps(TagsList, ensure_ascii=False)
    url="https://ani.gamer.com.tw/"+listUrl[i]
    dfAll=dfAll.append({"Platform":"anime_gamer","Title":title,"Tags":jsonArr,"URL":url}, ignore_index=True)
    dfAll.drop_duplicates(subset='URL',inplace=True)
    #print(listTitle[i])
    #print("https://ani.gamer.com.tw/"+listUrl[i])
print(dfAll.to_json())
'''