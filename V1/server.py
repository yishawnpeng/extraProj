import flask 
from flask import render_template, request
from flask_session import Session
from oneStudent import compileOneTime
#import os

def saveCode( code,studentID ) :
	codeFile = open(str(studentID)+".cpp", mode="w")
	codeFile.write(code)
	codeFile.close

app = flask.Flask(__name__)
sess=Session()

@app.route( "/", methods=["GET"] )
def home():
	return "Hi" 

@app.route( "/entrance", methods=["GET","POST"] )
def entrance():
	if request.method=="POST" :
		if request.values["send"]=="確認送出":
			#print(os.getcwd())
			saveCode(request.values["code"],10977030 )
			#print(os.getcwd())
			tempCode=request.values["code"]
			ans=''
			compileOneTime("10977030",ans)
			return render_template("/entrance.html", isSuccess="Success!", code=tempCode, result=ans ) 
	return render_template("/entrance.html", code="請輸入或上傳程式碼", result="結果" )

if __name__ == "__main__":
	app.config["DEBUG"] = True # if online this need to be false 
	app.config["JSON_AS_ASCII"] = False
	sess.init_app(app)
	app.run(host="0.0.0.0",port=5618)
	
