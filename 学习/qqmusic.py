# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:41:15 2019

@author: 24308
"""

import random
import requests
import time
import json

def get_pageA( url):
        html = requests.get(url, verify=False)
        # 如果请求网页正常，则继续后面的操作
        if html.status_code == 200:
            html.encoding = 'utf-8'
            return html
        return None


def get_page(key_url):
    html = requests.get(url)
    # # 请求网页状态为200，则进行编码和转换为字典
    if html.status_code == 200:
        html.encoding = 'utf-8'
        html = html.text
        html = json.loads(html)
        song_url = []
        # 获取vkey的位置
        vkey = html['req_0']['data']['midurlinfo'][0]['purl']
        url_head = 'http://ws.stream.qqmusic.qq.com/'
        Final_url = url_head + vkey
        song_url.append(Final_url)
        print("请耐心等待。。")
        print(song_url)
        download_link=[]
        download_link.append((name,Final_url))
def download(all_url,download_link):
    for url in download_link:
            music_name = url[0]
            url = url[1]
            time.sleep(1)
            # 请求网页
            res = get_page(url)
            res.encoding = 'utf-8'
            result = res.content
            # 开始下载，二进制格式
            with open('%s.mp3' % music_name, 'wb') as f:
                f.write(result)
                print('%s下载成功.mp3' % music_name)

name=input("请输入你要下载的歌曲或歌手的名字：")
try:
    print("请输入1-60的数字：")
    num=int(input(str("请输入要下载的数量：（默认为1）")))
except:
    num=1
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&p=1&n=%s&w=%s&format=json' % (num, name)
def get_agent():
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    fakeheader = {}
    fakeheader['User-agent'] = agents[random.randint(0, len(agents))]
    return fakeheader
headers=get_agent()
print(headers)

response=requests.get(url,headers=headers)
html=response.text
js=json.loads(html)

songlist=js["data"]["song"]["list"]
albummid=[]
for song in songlist:
    name=song["albumname"]
    mid=song["albummid"]
    albummid.append((name,mid))  
print(albummid)

for mid in  albummid:
    name=mid[0]
    songmid=mid[1]
    print(songmid)
    key_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?&data={"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8712940350","songmid":["%s"],"uin":"123"}},"comm":{"uin":123}}' % songmid
    print(key_url)                                                                                                                              

                                                                                                                             
