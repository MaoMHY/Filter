import paddlehub as hub

with open("./static/danmu/xiaocao.txt", 'r', encoding='UTF-8') as f:
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
