# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests


class NewscrapyPipeline(object):
    def process_item(self, item, spider):
        print("终于执行我了*****************************************************")
        base_dir=os.getcwd()
        filename=base_dir+"\data\weather.txt"
        print(filename)
        print(item["date"][0])
        for i in range(7):
            with open(filename, 'a',encoding="utf-8") as f:
                    f.write(item['date'][i] + '\n')
                    f.write(item['week'][i] + '\n')
                    f.write((item['temperature'][i]+ '\n'))
                    f.write(item['weather'][i] + '\n')
                    f.write(item['wind'][i] + '\n\n')
            print(type(item["temperature"][i][0]))
        # 下载图片
       
            with open(base_dir + '/data/' + item['date'][i] + '.png', 'wb') as f:
                f.write(requests.get("http:"+item['img'][i]).content)
            
        return item
