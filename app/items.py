# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AppItem(scrapy.Item):
    com_score=scrapy.Field()
    com_content=scrapy.Field()
    com_time=scrapy.Field()
    com_weight=scrapy.Field()
    com_likes=scrapy.Field()
    com_ver=scrapy.Field()
    pass
