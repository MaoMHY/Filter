import paddlehub as hub

<<<<<<< HEAD
with open("./static/danmu/xiaocao.txt", 'r', encoding='UTF-8') as f:
=======
import json
import threading
import requests


tokenurl="https://wenxin.baidu.com/younger/portal/api/oauth/token"
tokendata={
    "grant_type":"client_credentials",
    "client_id":"*****************************",
    "client_secret":"*****************************"
}
token_res=requests.request("POST",tokenurl,data=tokendata)
access_token=json.loads(token_res.text)["data"]



url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernie/3.0/zeus"

with open("./static/danmu/我是一棵小草.txt", 'r', encoding='UTF-8') as f:
>>>>>>> 97a3d491569d7c66ac1ba6f225be78e5a6cbce82
    danmulist = [i.strip() for i in f.readlines()]
with open("./static/danmu/time.txt", 'r', encoding='UTF-8') as f:
    time_of_danmu = [float(i) for i in f.readlines()]

danmulistindex=[]

senta = hub.Module(name="senta_bilstm")
results = senta.sentiment_classify(texts=danmulist, use_gpu=False,batch_size=1)
for i in range(0,len(results)):
    try:
        print(results[i]['text'])
        res=results[i]['sentiment_label']
        print(res)
        if res==1:
            danmulistindex.append(i)
    except Exception as e:
        # pass
        print(e)
    else:
        print(" ")

for i in range(0,len(danmulistindex)):
    with open("./static/danmu/xiaocao2.txt", 'a', encoding='UTF-8') as f:
        f.write(danmulist[danmulistindex[i]]+"\n")
    with open("./static/danmu/time2.txt", 'a', encoding='UTF-8') as f:
        f.write(str(time_of_danmu[danmulistindex[i]])+"\n")
<<<<<<< HEAD
=======


# payload={
#     'text': '卓越的发货速度实在是太慢了！预计发货时间有什么意义呢？形同虚设！春节期间就不能多雇点人保证服务质量吗？大过年的你这一拖搞的大家都不爽！ 这是好评吗？ ',
#     'seq_len': 8,
#     'task_prompt': 'SentimentClassification',
#     'dataset_prompt': '',
#     'access_token': access_token,
#     # 'topk': 1,
#     'stop_token': ''
#     }

# response = requests.request("POST", url, data=payload)
# res=json.loads(response.text)["data"]["result"]

# print(res)
>>>>>>> 97a3d491569d7c66ac1ba6f225be78e5a6cbce82
