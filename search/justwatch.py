from justwatch import JustWatch
import json
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


just_watch = JustWatch(country='TW')

results = just_watch.search_for_item(query='搖曳露營')
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
if results['total_results']>=30:
	max=30
else:
	max=results['total_results']
dfAll = pd.DataFrame()
for i in range(0,max):

	title=results['items'][i]['title']
	print(title)
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
		print(df)
		dfAll=dfAll.append({"Title":title,"Watch":df}, ignore_index=True)
	except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
		print('沒有URL')
	print("***********")
print(dfAll)