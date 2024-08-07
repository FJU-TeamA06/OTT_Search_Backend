from justwatch import JustWatch
import json
import pandas as pd
import warnings
from bilibili_api import search, sync
import requests
from bs4 import BeautifulSoup
from youtubesearchpython import PlaylistsSearch
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings("ignore")
dfAll_Final = pd.DataFrame()
def searchJW(SearchKeyword):
	dfAll = pd.DataFrame()
	
	#justwatch(用justwatchAPI抓取)
	just_watch = JustWatch(country='TW')
	results = just_watch.search_for_item(query=SearchKeyword)
	str1 = json.dumps(results)
	str2 = json.dumps(results['items'])
	if results['total_results']>=3:
		max=3
	else:
		max=results['total_results']
	for i in range(0,max):

		title=results['items'][i]['title']
		#print(title)
		#df = pd.DataFrame(results['items'][i]['offers'])
		#print(df.columns)
		#print("=====================")
		try:
			for j in range(len(results['items'][i]['offers'])):
				url=results['items'][i]['offers'][j]['urls']['standard_web']
				platform=results['items'][i]['offers'][j]['package_short_name']
				#print(platform)
				#print(url)
				dfAll=dfAll.append({"Platform":platform,"Title":title,"Tag":SearchKeyword,"URL":url}, ignore_index=True)
				dfAll=dfAll.append({"Platform":platform,"Title":title,"Tag":title,"URL":url}, ignore_index=True)
				dfAll.drop_duplicates(inplane=True)
		except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
			pass
		#print("***********")
	global dfAll_Final
	dfAll_Final=dfAll_Final.append(dfAll)
def searchBiliBili(SearchKeyword):
	dfAll = pd.DataFrame()
	#BiliBili(用bilibili_api抓取)
	async def test_f_search_by_order():
		return await search.search_by_type(SearchKeyword, search_type=search.SearchObjectType.BANGUMI)
	listTitle=[]
	listUrl=[]

	res = sync(test_f_search_by_order())
	#print(res['result'])
	try:
		str1 = json.dumps(res['result'])
		#print(str1)
		if len(res['result'])>=5:
			max=5
		else:
			max=len(res['result'])

		for i in range(0,max):
			title=res['result'][i]['title']

			title = title.replace('<em class="keyword">',"")
			title = title.replace('</em>',"")
			#print(title)
			url=res['result'][i]['url']
			dfAll=dfAll.append({"Platform":"BiliBili","Title":title,"Tag":title,"URL":url}, ignore_index=True)
			dfAll=dfAll.append({"Platform":"BiliBili","Title":title,"Tag":SearchKeyword,"URL":url}, ignore_index=True)

			#dfAll.drop_duplicates(subset='URL',inplace=True)
			#print(title)
			#print(url)
			#print("-----")
	except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
		pass
	global dfAll_Final
	dfAll_Final=dfAll_Final.append(dfAll)


def searchAnimeGamer(SearchKeyword):
	dfAll = pd.DataFrame()
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
		title=listTitle[i]
		url="https://ani.gamer.com.tw/"+listUrl[i]
		dfAll=dfAll.append({"Platform":"anime_gamer","Title":title,"Tag":title,"URL":url}, ignore_index=True)
		dfAll=dfAll.append({"Platform":"anime_gamer","Title":title,"Tag":SearchKeyword,"URL":url}, ignore_index=True)
		#dfAll.drop_duplicates(subset='URL',inplace=True)

	    #print(listTitle[i])
	    #print("https://ani.gamer.com.tw/"+listUrl[i])


	global dfAll_Final
	dfAll_Final=dfAll_Final.append(dfAll)



def searchYoutube(SearchKeyword):
	dfAll = pd.DataFrame()
	#Youtube搜尋(羚邦&木棉花)
	searchYT = PlaylistsSearch(SearchKeyword)
	res=searchYT.result()
	try:
		for i in range(0,len(res['result'])):
			df = pd.DataFrame()
			if res['result'][i]['channel']['id'] == "UCgdwtyqBunlRb-i-7PnCssQ":
				#print("MuseYT")
				#print(res['result'][i]['title'])
				#print(res['result'][i]['link'])
				title=res['result'][i]['title']
				url=res['result'][i]['link']

				dfAll=dfAll.append({"Platform":"MuseYT","Title":title,"Tag":title,"URL":url}, ignore_index=True)

				dfAll=dfAll.append({"Platform":"MuseYT","Title":title,"Tag":SearchKeyword,"URL":url}, ignore_index=True)
				#dfAll.drop_duplicates(subset='URL',inplace=True)

			if res['result'][i]['channel']['id'] == "UC0wNSTMWIL3qaorLx0jie6A":
				#print("AniOneYT")
				#print(res['result'][i]['title'])
				#print(res['result'][i]['link'])
				title=res['result'][i]['title']
				url=res['result'][i]['link']
				dfAll=dfAll.append({"Platform":"AniOneYT","Title":title,"Tag":title,"URL":url}, ignore_index=True)
				dfAll=dfAll.append({"Platform":"AniOneYT","Title":title,"Tag":SearchKeyword,"URL":url}, ignore_index=True)
				#dfAll.drop_duplicates(subset='URL',inplace=True)
	except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
		pass	

	
	global dfAll_Final
	dfAll_Final=dfAll_Final.append(dfAll)
def searchOTT(text):

	

	SearchKeyword=text
	'''
	try:
		dfAll=dfAll.append(searchJW(text))
		dfAll=dfAll.append(searchBiliBili(text))
		dfAll=dfAll.append(searchAnimeGamer(text))
		dfAll=dfAll.append(searchYoutube(text))


		


		
		




		#print(dfAll)
		#print("/////////////////")
		#print(dfAll.to_json())
	except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
			pass
	'''
	global dfAll_Final
	with ThreadPoolExecutor() as executor:    # 改用 with...as
		executor.submit(searchJW, text)
		executor.submit(searchBiliBili, text)
		executor.submit(searchAnimeGamer, text)
		executor.submit(searchYoutube, text)
		
	
	return dfAll_Final