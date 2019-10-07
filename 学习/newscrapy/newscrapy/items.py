# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date=scrapy.Field()
    week=scrapy.Field()
    img=scrapy.Field()
    temperature=scrapy.Field()
    weather=scrapy.Field()
    wind=scrapy.Field()
    
