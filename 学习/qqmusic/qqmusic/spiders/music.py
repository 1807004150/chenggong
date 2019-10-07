# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:54:38 2019

@author: 24308
"""
import scrapy
import requests
from scrapy.http import Request
import json
from qqmusic.items import QqmusicItem

class MusicSpider(scrapy.Spider):
    name="music"    
    songer=input("请输入你要下载的歌曲或歌手的名字：")
    all_download_link=[]
    all_songmid=[]
    print("请输入1-60的数字：")
    num=int(input(str("请输入要下载的数量：（默认为1）")))
    start_urls=['https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&p=1&n=%s&w=%s&format=json' % (num,songer),]
    def parse(self,response):
        print("开始了")
     
        self.item= QqmusicItem()
        res = response.text
        html = json.loads(res)
        for i in range(len(html['data']['song']['list'])):
            songmid = html['data']['song']['list'][i]['songmid']
            songname = html['data']['song']['list'][i]['songname']
            self.all_songmid.append((songname, songmid))
        print(songmid)
        for mid in self.all_songmid:
            self.name = mid[0]
            self.songmid = mid[1]
            # 这个url是获取vkey的url，取结果拼凑成music下载链接
            self.vkey_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?&data={"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8712940350","songmid":["%s"],"uin":"123"}},"comm":{"uin":123}}' % songmid
            print(self.vkey_url)
        
        return Request(self.vkey_url,callback=self.parse_2)
    def parse_2(self,response):
           
            res=response.text
            
            html = json.loads(res)
            vkey = html['req_0']['data']['midurlinfo'][0]['purl']
            # 拼凑music下载链接
            self.music_link = 'http://ws.stream.qqmusic.qq.com/' + vkey
            # 将music下载链接添加到列表
            self.all_download_link.append((self.name, self.music_link))
            self.item["link"]=self.music_link
            self.item["songmid"]=self.songmid
            self.item["vkey"]=vkey
            return self.item
        

        
    