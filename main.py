# coding:utf-8
from flask import Flask,request,json,render_template,session,jsonify
import os

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY','secret string')
app.config['SESSION_TYPE'] = 'filesystem'
app.config["SECRET_KEY"] = "jjjsks"

@app.route("/")
def index():
    return render_template("VideoPage.html")

@app.route("/getDanmu")
def getDanmu():
    with open("./static/danmu/xiaocao.txt", 'r', encoding='UTF-8') as f:
        danmulist = [i.strip() for i in f.readlines()]
    with open("./static/danmu/time.txt", 'r', encoding='UTF-8') as f:
        time_of_danmu = [float(i) for i in f.readlines()]
    danmu=[]
    for i in range(0,len(danmulist)):
        danmu.append({
            "text": danmulist[i],
			"color": "white",
			"size": 1,
			"position": 0,
			"time":int(time_of_danmu[i])
        })
    return {"danmu":danmu}

@app.route("/getDanmuFilter")
def getDanmuFilter():
    with open("./static/danmu/xiaocao2.txt", 'r', encoding='UTF-8') as f:
        danmulist = [i.strip() for i in f.readlines()]
    with open("./static/danmu/time2.txt", 'r', encoding='UTF-8') as f:
        time_of_danmu = [float(i) for i in f.readlines()]
    danmu=[]
    for i in range(0,len(danmulist)):
        # if danmu_is_ok(danmulist[i]): 
        danmu.append({
            "text": danmulist[i],
            "color": "white",
            "size": 1,
            "position": 0,
            "time":int(time_of_danmu[i])
        })
        
    return {"danmu":danmu}


if __name__ == '__main__':
    app.run(debug=True)