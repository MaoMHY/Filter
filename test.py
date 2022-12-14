# -*- coding: utf-8 -*
import threading

import wenxin_api
from wenxin_api.tasks.text_generation import TextGeneration

wenxin_api.ak = "***************************"
wenxin_api.sk = "***************************"

with open("./static/danmu/xiaocao.txt", 'r', encoding='UTF-8') as f:
    danmulist = [i.strip() for i in f.readlines()]
with open("./static/danmu/time.txt", 'r', encoding='UTF-8') as f:
    time_of_danmu = [float(i) for i in f.readlines()]

danmulistindex=[]


def danmu_is_ok(danmu):
    payload={
        "text": danmu+" 这是好评吗？ ",
        "seq_len": 512,
		"topp": 0,
		"min_dec_len": 2,
		"is_unidirectional": 0,
		"task_prompt": "SentimentClassification",
		"min_dec_penalty_text": "",
		"penalty_text": "",
		"mask_type": "word",
		"logits_bias": 0
        }
    try:
        rst = TextGeneration.create(**payload)
        res=rst["result"].strip()
    except Exception as e:
        return False
        # pass
    else:
        print(res)
        if(res=="是"):
            return True
        else:
            return False

def fun1():
    for i in range(0,50):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)
def fun2():
    for i in range(50,100):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)
def fun3():
    for i in range(100,150):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)
def fun4():
    for i in range(150,200):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)
def fun5():
    for i in range(200,250):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)
def fun6():
    for i in range(250,300):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)
def fun7():
    for i in range(300,350):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)
def fun8():
    for i in range(350,400):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)
def fun9():
    for i in range(400,450):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)
def fun10():
    for i in range(450,500):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)
def fun11():
    for i in range(500,550):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)
def fun12():
    for i in range(550,600):
        if danmu_is_ok(danmulist[i]):
            danmulistindex.append(i)

t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t3 = threading.Thread(target=fun3)
t4 = threading.Thread(target=fun4)
t5 = threading.Thread(target=fun5)
t6 = threading.Thread(target=fun6)
t7 = threading.Thread(target=fun7)
t8 = threading.Thread(target=fun8)
t9 = threading.Thread(target=fun9)
t10 = threading.Thread(target=fun10)
t11 = threading.Thread(target=fun11)
t12 = threading.Thread(target=fun12)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()

for i in range(0,len(danmulistindex)):
    with open("./static/danmu/xiaocao2.txt", 'a', encoding='UTF-8') as f:
        f.write(danmulist[danmulistindex[i]]+"\n")
    with open("./static/danmu/time2.txt", 'a', encoding='UTF-8') as f:
        f.write(str(time_of_danmu[danmulistindex[i]])+"\n")
