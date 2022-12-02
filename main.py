from typing import Optional

from fastapi import FastAPI
import search
import searchDB
import sys

from fastapi.responses import HTMLResponse


app = FastAPI() # 建立一個 Fast API application

@app.get("/") # 指定 api 路徑 (get方法)
def read_root():
    return {"Hello": "World"}


@app.get("/getkeyword", response_class=HTMLResponse) # 指定 api 路徑 (get方法)
def read_keyword(keyword: Optional[str] = None):
    return searchDB.searchDB(keyword)