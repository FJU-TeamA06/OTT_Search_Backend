#番劇:Anime
from bilibili_api import search, sync
import json
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
dfAll = pd.DataFrame()
Keyword="公主連結"
async def test_f_search_by_order():
    return await search.search_by_type(Keyword, search_type=search.SearchObjectType.BANGUMI)


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
		TagsList=[]
		title=res['result'][i]['title']

		title = title.replace('<em class="keyword">',"")
		title = title.replace('</em>',"")
		print(title)
		TagsList.append(Keyword)
		TagsList.append(title)
		jsonArr = json.dumps(TagsList, ensure_ascii=False)
		print(jsonArr)
		url=res['result'][i]['url']
		dfAll=dfAll.append({"Platform":"BiliBili","Title":title,"Tags":jsonArr,"URL":url}, ignore_index=True)
		dfAll.drop_duplicates(subset='URL',inplace=True)
		print(title)
		print(url)
		print("-----")


except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
	pass
print(dfAll)
print("/////////////////")
print(dfAll.to_json())