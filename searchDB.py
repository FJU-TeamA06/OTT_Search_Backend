import pymysql
import pandas as pd
import search
import warnings
import csv
import json
import datetime
import time
from opencc import OpenCC

cc = OpenCC('s2tw')
warnings.filterwarnings("ignore")
#資料庫連線設定
#可縮寫db = pymysql.connect("localhost","root","root","30days" )

#建立操作游標

def searchDB(text,scrape):
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='Andy_Ching-0826', db='test_db', charset='utf8', autocommit=True)
    cursor = db.cursor()
    keyword=text


    
    
    #動態新增資料的程式碼，對效能影響巨大(大約增加8秒-60秒鐘不等)
    if scrape == 1:
        print("抓取選項為啟用")
        #底下被爬蟲，約1秒鐘
        ct = datetime.datetime.now()
        print("爬蟲開始")
        print("current time:-", ct)
        WebSearchDF=search.searchOTT(keyword);
        ct = datetime.datetime.now()
        print("爬蟲結束")
        print("current time:-", ct)
        print("----------")
        print(WebSearchDF.to_json(orient="table"))
        print("檢查和新增資料到DB開始")
        i=1
        for row in WebSearchDF.itertuples():
            print("第"+str(i)+"項，共"+str(len(WebSearchDF.index))+"項")
            #pass
            #print(getattr(row, 'Platform'), getattr(row, 'Title'), getattr(row, 'Tag'), getattr(row, 'URL')) # 输出每一行
            #print("------")
            Platform=getattr(row, 'Platform')
            Title=getattr(row, 'Title')
            Tag=getattr(row, 'Tag')
            URL=getattr(row, 'URL')
            
            args=(Title,Tag,Platform,URL)
            #result_args = cursor.callproc('Check_and_Add_Data',(args))
            sql="CALL Check_and_Add_Data(%s,%s,%s,%s);"
            cursor.execute(sql,(Title,Tag,Platform,URL))
            i=i+1
            #cursor.execute(sql)
            #print(result_args)
        #args=(keyword)
        time.sleep(0.1)
        print("檢查和新增資料到DB結束")
    else:
        print("抓取選項為禁用")



    ct = datetime.datetime.now()
    
    print("current time:-", ct)
    print("...")
    ResultPD=pd.DataFrame()
    ResultPD_Sorted=pd.DataFrame()
    try:
        #參數化查詢，防止SQL注入
        sql="CALL SearchTag(%s);"
        cursor.execute(sql,(keyword,))
        print("抓到資料了")
        for result in cursor.fetchall():
            #print(result[1]+"_"+result[3]+"_"+result[4])
            platform=result[3]
            #print(platform)
            platform=platform.replace("anime_gamer", "巴哈姆特動畫瘋")
            platform=platform.replace("nfx","Netflix")
            platform=platform.replace("gimytv","Gimy 劇迷")
            platform=platform.replace("imaple","楓林網")
            platform=platform.replace("line_TV","Line TV")
            platform=platform.replace("lin","Line TV")
            platform=platform.replace("kkt","KKTV")
            platform=platform.replace("prv","Amazon Prime Video")
            platform=platform.replace("dnp","Disney+")
            platform=platform.replace("itu","iTunes")
            platform=platform.replace("zee","Zee5")
            platform=platform.replace("MuseYT","木棉花YouTube官方頻道")
            platform=platform.replace("AniOneYT","羚邦YouTube官方頻道")
            platform=platform.replace("mbi","MUBI")
            platform=platform.replace("cla","Classix")
            #print(platform)
            ResultPD=ResultPD.append({"Platform":platform,"Title":cc.convert(result[1]),"URL":result[4]}, ignore_index=True)
        ResultPD_Sorted=ResultPD.sort_values(by='Platform')
    except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
            pass
    db.close()
    
    print(ResultPD_Sorted)
    ct = datetime.datetime.now()
    print("資料整理完成")
    print("current time:-", ct)
    return(ResultPD_Sorted.to_json(orient="table"));