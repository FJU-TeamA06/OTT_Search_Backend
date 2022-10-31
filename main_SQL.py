import search
import sys
from sqlalchemy import create_engine, text
import pandas as pd

df_search=pd.DataFrame()
engine = create_engine('mysql+pymysql://[帳號]:[密碼]@[SQL的IP]:[PORT]/testdb')
search_tag=sys.argv[1]
search_List=[]
search_List.append(search_tag)
sql_query = "SELECT * FROM SearchResult WHERE Tags LIKE '%"+search_tag+"%';"

print(text(sql_query))
df_read = pd.read_sql_query(text(sql_query), engine)



if df_read.empty:
	sql_ALL = "SELECT * FROM SearchResult"
	df_read = pd.read_sql_query(text(sql_ALL), engine)
	df_search=search.searchOTT(sys.argv[1])

	#df_write=pd.merge(df_read,search.searchOTT(sys.argv[1]), on='Title')
	df_new=df_read.append(df_search)
	df_new.drop_duplicates(subset='Watch',inplace=True)
	df_new.to_sql('SearchResult', engine, index=False,if_exists='replace')
	sql_query = "SELECT * FROM SearchResult WHERE Tags LIKE '%"+search_tag+"%';"
	df_read = pd.read_sql_query(text(sql_query), engine)
	print(df_read)
else:
	print(df_read)
