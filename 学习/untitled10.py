# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:15:46 2019

@author: 24308
"""

# author   sunrisecai
import json
import time
import requests


class QQ_Music_Spider():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64;Trident/7.0;rv:11.0) like Gecko'}
        self.all_songmid = []  # 存放所有songmid
        self.all_download_link = []  # 存放所有音乐下载链接

    def get_page(self, url, headers):
        html = requests.get(url, headers=self.headers, verify=False)
      
        if html.status_code == 200:
            html.encoding = 'utf-8'
            return html
        return None

    def music_number(self):
        try:
            print("==请输入1-60的数字，不在此范围或不输入默认为1==")
            num = int(input("请输入下载歌曲的数目(最大为60,回车默认为1):"))
            if 0 < int(num) < 60:
                return num
        except:
            num = 1
            return num

    def get_songmid(self, num, name):
        # 这个url是搜索页
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&p=1&n=%s&w=%s&format=json' % (num, name)
        res = self.get_page(url, headers=self.headers).text
        html = json.loads(res)
        print(html)
        for i in range(len(html['data']['song']['list'])):
            songmid = html['data']['song']['list'][i]['songmid']
            songname = html['data']['song']['list'][i]['songname']
            self.all_songmid.append((songname, songmid))

    def get_mid_vkey(self):
        # 遍历所有的songmid，拼凑成获取vkey的url
        for mid in self.all_songmid:
            name = mid[0]
            songmid = mid[1]
            print(songmid)
            # 这个url是获取vkey的url，取结果拼凑成music下载链接
            vkey_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?&data={"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8712940350","songmid":["%s"],"uin":"123"}},"comm":{"uin":123}}' % songmid
            print(vkey_url)                                                                                                                               
            res = self.get_page(vkey_url, headers=self.headers)
            res.encoding = 'utf-8'
            result = res.text
            html = json.loads(result)
            vkey = html['req_0']['data']['midurlinfo'][0]['purl']
            # 拼凑music下载链接
            music_link = 'http://ws.stream.qqmusic.qq.com/' + vkey
            # 将music下载链接添加到列表
            self.all_download_link.append((name, music_link))

    def download(self):
        # 遍历music下载链接列表
        for url in self.all_download_link:
            music_name = url[0]
            url = url[1]
            time.sleep(1)
            # 请求网页
            res = self.get_page(url, headers=self.headers)
            res.encoding = 'utf-8'
            result = res.content
            # 开始下载，二进制格式
            with open('%s.mp3' % music_name, 'wb') as f:
                f.write(result)
                print('%s下载成功.mp3' % music_name)
 num = self.music_number()
 name = input("请输入歌手或歌曲名字：")
 self.get_songmid(num, name)
 self.get_mid_vkey()
 self.download()


# 执行主函数
if __name__ == '__main__':
    spider = QQ_Music_Spider()
    spider.main()
