import pymysql
import pandas as pd
import search
import warnings
import csv
import json
import time
warnings.filterwarnings("ignore")
#資料庫連線設定
#可縮寫db = pymysql.connect("localhost","root","root","30days" )

#建立操作游標

def searchDB(text):
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='Andy_Ching-0826', db='test_db', charset='utf8', autocommit=True)
    cursor = db.cursor()
    keyword=text
    WebSearchDF=search.searchOTT(keyword);
    for row in WebSearchDF.itertuples():
        #pass
        #print(getattr(row, 'Platform'), getattr(row, 'Title'), getattr(row, 'Tag'), getattr(row, 'URL')) # 输出每一行
        #print("------")
        Platform=getattr(row, 'Platform')
        Title=getattr(row, 'Title')
        Tag=getattr(row, 'Tag')
        URL=getattr(row, 'URL')
        
        args=(Title,Tag,Platform,URL)
        result_args = cursor.callproc('Check_and_Add_Data',(args))
        #cursor.execute(sql)
        #print(result_args)
    #args=(keyword)
    cursor.execute("CALL SearchTag(\""+keyword+"\");")
    ResultPD=pd.DataFrame()
    for result in cursor.fetchall():
        #print(result[1]+"_"+result[3]+"_"+result[4])
        ResultPD=ResultPD.append({"Platform":result[3],"Title":result[1],"URL":result[4]}, ignore_index=True)
    db.close()
    ResultPD_Sorted=ResultPD.sort_values(by='Platform')
    print(ResultPD_Sorted)
    return(ResultPD_Sorted.to_json(orient="table"));
    '''
    cursor.execute("call searchTag(\"給不滅\");")
    for result in cursor.fetchall():
        print(result)
    
    #return(WebSearchDF.to_json(orient="table"))
    '''
    '''
    #SQL語法（查詢資料庫版本）
    sql = "Select DISTINCT titletable.Mid,titletable.Title,tagstable.Tag,watchtable.Platform,watchtable.URL \
    from tagstable, watchtable,titletable \
    Where tagstable.Mid = watchtable.Mid and tagstable.Mid = titletable.Mid and tagstable.Tag like \"%"+keyword+"%\"";
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        rowCount = len(results)
        df = pd.DataFrame()
        if rowCount != 0:
            for row in results:
                #print (row)
                Mid = row[0]
                Title=row[1]
                Tag = row[2]
                Platform = row[3]
                URL = row[4]
                # Now print fetched result
                df=df.append({"Mid":Mid,"Title":Title,"Tag":Tag,"Platform":Platform,"URL":URL}, ignore_index=True)
                print ("Mid = %s,Tag = %s,Platform = %s,URL = %s" % \
                        (Mid, Tag,Platform, URL ))
            fieldnames = ("Mid","Title","Tag","Platform","URL")
            return(df.to_json(orient="table"))
        else:
            return("Not Found")
                
    except:
       import traceback
       traceback.print_exc()

       return ("Error: unable to fetch data")

    # disconnect from server
    db.close()
    '''