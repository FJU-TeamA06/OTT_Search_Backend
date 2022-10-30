#番劇:Anime
from bilibili_api import search, sync
import json
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
dfAll = pd.DataFrame()

async def test_f_search_by_order():
    return await search.search_by_type("公主連結", search_type=search.SearchObjectType.BANGUMI)
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
	print(df)
	dfAll=dfAll.append({"Title":listTitle[i],"Watch":df}, ignore_index=True)
    
print(dfAll)
print("/////////////////")
print(dfAll.to_json())