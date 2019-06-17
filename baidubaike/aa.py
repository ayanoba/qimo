# -*- coding=utf-8 -*-
import requests
import re
import time
from bs4 import BeautifulSoup
time1 = time.time()
exist_url = []
g_writercount = 0
def scrappy(url, depth = 1):
    global g_writercount
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        r = requests.get(url, headers=headers)
        #html = r.content.decode('utf-8')
        html = r.text.encode('utf-8').decode(requests.utils.get_encodings_from_content(r.text)[0])
        # print(html)
    except Exception as e:
        print(e)
        print('下载失败:' + url)
        return None
    finally:
        exist_url.append(url)
    link_list = re.findall('.*?<a target=_blank href="/item/([^:#=<>]*?)".*?</a>', html)
    unique_list = list(set(link_list) - set(exist_url))

    for eachone in unique_list:
        g_writercount += 1
        output = "No." + str(g_writercount) + "\t Depth:" + str(depth) + "\t" + url + ' - > ' + eachone + "\n"
        print(output)
        with open('url.txt', "a+") as f:
            f.write(output)
            f.close()
        if depth < 2:
            scrappy("https://baike.baidu.com/item/"+eachone, depth+1)

scrappy("https://baike.baidu.com/item/百度百科")
time2 = time.time()
print("时间:", time2-time1)