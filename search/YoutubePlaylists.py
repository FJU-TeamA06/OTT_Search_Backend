from youtubesearchpython import PlaylistsSearch
import json
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
dfAll = pd.DataFrame()

#木棉花
#UCgdwtyqBunlRb-i-7PnCssQ
#羚邦
#UC0wNSTMWIL3qaorLx0jie6A

search = PlaylistsSearch('搖曳露營')
res=search.result()
try:
	for i in range(0,len(res['result'])):
		df = pd.DataFrame()
		if res['result'][i]['channel']['id'] == "UCgdwtyqBunlRb-i-7PnCssQ":
			print("MuseYT")
			print(res['result'][i]['title'])
			print(res['result'][i]['link'])
			url=res['result'][i]['link']
			df = df.append({"Platform":"MuseYT","URL":url}, ignore_index=True)
			print(df)
			dfAll=dfAll.append({"Title":res['result'][i]['title'],"Watch":df}, ignore_index=True)

		if res['result'][i]['channel']['id'] == "UC0wNSTMWIL3qaorLx0jie6A":
			print("AniOneYT")
			print(res['result'][i]['title'])
			print(res['result'][i]['link'])
			url=res['result'][i]['link']
			df = df.append({"Platform":"AniOneYT","URL":url}, ignore_index=True)
			print(df)
			dfAll=dfAll.append({"Title":res['result'][i]['title'],"Watch":df}, ignore_index=True)
except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
	pass			
print(dfAll)
print("/////////////////")
print(dfAll.to_json())