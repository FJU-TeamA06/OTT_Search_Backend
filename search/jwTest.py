from justwatch import JustWatch
import random
import pandas as pd
import warnings
from tqdm import tqdm, trange
import time
warnings.filterwarnings("ignore")
just_watch = JustWatch(country='TW')
dfAll = pd.DataFrame()

for h in trange(1,66):
	print("------")
	results_by_providers = just_watch.search_for_item(page=h,providers=['kkt'])
	#print(results_by_providers)
	max=results_by_providers['page_size']
	for i in range(0,max):
		try:
			title=results_by_providers['items'][i]['title']
			print(title)
			#print(results_by_providers['items'][i]['id'])
		
			megamind = just_watch.get_title(title_id=results_by_providers['items'][i]['id'])
			#print(megamind['offers'])
			for j in range(len(megamind['offers'])):
				url=megamind['offers'][j]['urls']['standard_web']
				platform=megamind['offers'][j]['package_short_name']
				if platform == "kkt":
					print(platform)
					print(url)
					dfAll=dfAll.append({"Platform":platform,"Title":title,"URL":url}, ignore_index=True)
					dfAll.drop_duplicates(subset='Title',inplace=True)
					dfAll.to_csv("./kkTV_All.csv", encoding = 'utf-8',index = True)
		except:
			pass
	waitTime=60+random.randrange(-10,10)
	print("第"+str(h)+"頁，共66頁")
	print("Wait "+str(waitTime)+" second")
	time.sleep(waitTime)

print(dfAll.to_csv())
dfAll.to_csv("./kkTV_All.csv", encoding = 'utf-8',index = True)