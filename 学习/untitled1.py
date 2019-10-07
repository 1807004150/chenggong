# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:13:06 2019

@author: 24308
"""

from bs4 import BeautifulSoup
import bs4
import requests
def get_url(url):
    try:
        r=requests.get(url,timeout=30)
        r.encoding="gbk"
        return r.text
    except:
        return "ERROR"
def get_content(url):
    html=get_url(url)
    soup=BeautifulSoup(html,"lxml")
    movies_list = soup.find('ul', class_='picList clearfix')
    movies = movies_list.find_all('li')
    
    for top in movies:
        img_url=top.find('img')['src']
        

        name = top.find('span',class_='sTit').a.text
        try:
            time = top.find('span',class_='sIntro').text
        except:
            time = "暂无上映时间"
        actors = top.find('p',class_='pActor')
        actor=""
        if  isinstance(actors,bs4.element.Tag):
                actors_list=[]
                for act in actors.contents:
                    actor =actor+act.string.replace("\r","").replace("\n","")+" "
                    
                    actors_list.append(actor)
                actor=actors_list[-1][0:3]+" "+actors_list[-1][3:-1].strip()
                intro = top.find('p',class_='pTxt pIntroShow').text
        with open("photo_.txt","a+",encoding="utf-8")as f:
            f.write("片名：{}\t{}\n{}\n{} \n \n ".format(name,time,actor,intro) )
        with open('C:\\Users\\24308\\Desktop\\photograph'+name+'.png','wb+') as f:
            f.write(requests.get("http:"+img_url).content)

url="http://dianying.2345.com/top/"
get_content(url)