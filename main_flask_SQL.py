import search
import searchDB
from flask import Flask
from flask import render_template
from flask import request
import sys

app = Flask(__name__)
@app.route("/getkeyword", methods=['GET'])
def getkeyword():
	keyword=request.args.get('keyword')
	return searchDB.searchDB(keyword)
if __name__ == "__main__":
# Port 監聽8088，並啟動除錯模式。
	#app.run(host="0.0.0.0",port=8088, debug=True,ssl_context=('server.crt', 'server.key'))
    app.run(host="0.0.0.0",port=8088, debug=True)
