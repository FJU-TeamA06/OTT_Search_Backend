from youtubesearchpython import PlaylistsSearch
import json
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
dfAll = pd.DataFrame()
Keyword="搖曳露營"
#木棉花
#UCgdwtyqBunlRb-i-7PnCssQ
#羚邦
#UC0wNSTMWIL3qaorLx0jie6A

search = PlaylistsSearch(Keyword)
res=search.result()
try:
	for i in range(0,len(res['result'])):
		df = pd.DataFrame()
		if res['result'][i]['channel']['id'] == "UCgdwtyqBunlRb-i-7PnCssQ":
			TagsList=[]
			print("MuseYT")
			print(res['result'][i]['title'])
			print(res['result'][i]['link'])
			title=res['result'][i]['title']
			url=res['result'][i]['link']
			TagsList.append(Keyword)
			TagsList.append(title)
			jsonArr = json.dumps(TagsList, ensure_ascii=False)


			dfAll=dfAll.append({"Platform":"MuseYT","Title":title,"Tags":jsonArr,"URL":url}, ignore_index=True)
			dfAll.drop_duplicates(subset='URL',inplace=True)

		if res['result'][i]['channel']['id'] == "UC0wNSTMWIL3qaorLx0jie6A":
			TagsList=[]
			print("AniOneYT")
			print(res['result'][i]['title'])
			print(res['result'][i]['link'])
			title=res['result'][i]['title']
			url=res['result'][i]['link']
			TagsList.append(Keyword)
			TagsList.append(title)
			jsonArr = json.dumps(TagsList, ensure_ascii=False)
			dfAll=dfAll.append({"Platform":"AniOneYT","Title":title,"Tags":jsonArr,"URL":url}, ignore_index=True)
			dfAll.drop_duplicates(subset='URL',inplace=True)
except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
	pass			
print(dfAll)
print("/////////////////")
print(dfAll.to_json())