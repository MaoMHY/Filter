# coding:utf-8
import re
from flask import Flask,request,json,render_template,session,jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import json
import requests
from sqlalchemy import false, true

tokenurl="https://wenxin.baidu.com/younger/portal/api/oauth/token"
tokendata={
    "grant_type":"client_credentials",
    "client_id":"1IFWlhc0WyXTa3i7xw3OeGTAuWp0KeY1",
    "client_secret":"sqPtDNcxK6AreUi4D6ZgHshDEvOKG7hK"
}
token_res=requests.request("POST",tokenurl,data=tokendata)
access_token=json.loads(token_res.text)["data"]
url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernie/3.0/zeus"

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY','secret string')
app.config['SESSION_TYPE'] = 'filesystem'
app.config["SECRET_KEY"] = "jjjsks"

@app.route("/")
def index():
    return render_template("VideoPage.html")

@app.route("/getDanmu")
def getDanmu():
    with open("./static/danmu/我是一棵小草.txt", 'r', encoding='UTF-8') as f:
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

def danmu_is_ok(danmu):
    payload={
        'text': danmu+' 这是好评吗？ ',
        'seq_len': 8,
        'task_prompt': 'SentimentClassification',
        'dataset_prompt': '',
        'access_token': access_token,
        # 'topk': 1,
        'stop_token': ''
        }
    response = requests.request("POST", url, data=payload)
    try:
        res=json.loads(response.text)["data"]["result"]
    except Exception as e:
        return False
        # pass
    else:
        print(res)
        if(res=="是"):
            return True
        else:
            return False
    # if response==None:
    #     return false
    # else:
    #     res=json.loads(response.text)["data"]["result"]
    #     print(res)
    #     if(res=="是"):
    #         return true
    #     else:
    #         return false

if __name__ == '__main__':
    app.run(debug=True)