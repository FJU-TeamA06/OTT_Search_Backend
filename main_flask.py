import search
from flask import Flask
from flask import render_template
from flask import request
import sys

app = Flask(__name__)
@app.route("/getkeyword", methods=['GET'])
def getkeyword():
	keyword=request.args.get('keyword')
	return search.searchOTT(keyword).to_json()
if __name__ == "__main__":
# Port 監聽8088，並啟動除錯模式。
	app.run(port=8088, debug=True)
