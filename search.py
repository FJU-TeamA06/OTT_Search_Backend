from justwatch import JustWatch
import json
import pandas as pd
import warnings
from bilibili_api import search, sync
import requests
from bs4 import BeautifulSoup
warnings.filterwarnings("ignore")
def searchOTT(text):

	dfAll = pd.DataFrame()

	SearchKeyword=text

	#justwatch(用justwatchAPI抓取)
	just_watch = JustWatch(country='TW')
	results = just_watch.search_for_item(query=SearchKeyword)
	str1 = json.dumps(results)
	str2 = json.dumps(results['items'])
	if results['total_results']>=30:
		max=30
	else:
		max=results['total_results']
	for i in range(0,max):

		title=results['items'][i]['title']
		#print(title)
		#df = pd.DataFrame(results['items'][i]['offers'])
		#print(df.columns)
		#print("=====================")
		try:
			listPatform=[]
			listUrl=[]
			for j in range(len(results['items'][i]['offers'])):
				url=results['items'][i]['offers'][j]['urls']['standard_web']
				patform=results['items'][i]['offers'][j]['package_short_name']
				#print(patform)
				#print(url)
				listPatform.append(patform)
				listUrl.append(url)
			df = pd.DataFrame({"Platform":listPatform,"URL":listUrl})
			df.drop_duplicates(subset='Platform',inplace=True)
			#print(df)
			dfAll=dfAll.append({"Title":title,"Watch":df}, ignore_index=True)
		except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
			pass
		#print("***********")


	#BiliBili(用bilibili_api抓取)
	async def test_f_search_by_order():
	    return await search.search_by_type(SearchKeyword, search_type=search.SearchObjectType.BANGUMI)
	listTitle=[]
	listUrl=[]

	res = sync(test_f_search_by_order())
	#print(res['result'])
	str1 = json.dumps(res['result'])
	#print(str1)
	if len(res['result'])>=30:
		max=30
	else:
		max=len(res['result'])

	for i in range(0,max):
		title=res['result'][i]['title']
		title = title.replace('<em class="keyword">',"")
		title = title.replace('</em>',"")
		listTitle.append(title)
		listUrl.append(res['result'][i]['url'])
		#print(title)
		#print(res['result'][i]['url'])
		#print("-----")
	for i in range(0,len(listTitle)):
		#print(listTitle[i])
		#print(listUrl[i])
		df = pd.DataFrame()
		url=listUrl[i]
		df = df.append({"Platform":"BiliBili","URL":url}, ignore_index=True)
		#print(df)
		dfAll=dfAll.append({"Title":listTitle[i],"Watch":df}, ignore_index=True)



	#動畫瘋(用BeautifulSoup爬取)
	listTitle=[]
	listUrl=[]
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
	}
	response = requests.get(
	    "https://ani.gamer.com.tw/search.php?keyword="+SearchKeyword, headers=headers)
	soup = BeautifulSoup(response.text, "html.parser")
	#print(soup.prettify())  #輸出排版後的HTML內容
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
	    df = pd.DataFrame()
	    url="https://ani.gamer.com.tw/"+listUrl[i]
	    df = df.append({"Platform":"anime_gamer","URL":url}, ignore_index=True)
	    #print(df)
	    dfAll=dfAll.append({"Title":listTitle[i],"Watch":df}, ignore_index=True)

	    #print(listTitle[i])
	    #print("https://ani.gamer.com.tw/"+listUrl[i])






	#print(dfAll)
	#print("/////////////////")
	#print(dfAll.to_json())
	return dfAll