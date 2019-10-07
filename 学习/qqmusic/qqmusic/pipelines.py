# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import requests

class QqmusicPipeline(object):
    def process_item(self, item, spider):
            res =requests.get(item["link"])
            res.encoding = 'utf-8'
            result = res.content
            # 开始下载，二进制格式
            with open('音乐.mp3','wb') as f:
                f.write(result)
                print('下载成功.mp3')
            return item
