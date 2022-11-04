from justwatch import JustWatch
import json
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

Keyword='搖曳露營'
just_watch = JustWatch(country='TW')

results = just_watch.search_for_item(query=Keyword)
#print(results)
str1 = json.dumps(results)
'''
print(str1)
print(type(str1))
print("--------------")
print(results['items'])
'''
str2 = json.dumps(results['items'])
'''
print("--------------------------")
print(str2)
print(type(str2))
print("--------------------------")
'''
if results['total_results']>=3:
	max=3
else:
	max=results['total_results']


dfAll = pd.DataFrame()
for i in range(0,max):
	TagsList=[]
	title=results['items'][i]['title']
	print(title)
	#df = pd.DataFrame(results['items'][i]['offers'])
	#print(df.columns)
	#print("=====================")
	TagsList.append(Keyword)
	TagsList.append(title)
	jsonArr = json.dumps(TagsList, ensure_ascii=False)
	try:
		for j in range(len(results['items'][i]['offers'])):
			url=results['items'][i]['offers'][j]['urls']['standard_web']
			patform=results['items'][i]['offers'][j]['package_short_name']
			print(patform)
			print(url)
			dfAll=dfAll.append({"Platform":patform,"Title":title,"Tags":jsonArr,"URL":url}, ignore_index=True)
			dfAll.drop_duplicates(subset='Platform',inplace=True)
		
	except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
		print('沒有URL')
	print("***********")
print(dfAll)