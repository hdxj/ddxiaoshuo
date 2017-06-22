# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingItem(scrapy.Item):
    name = scrapy.Field()
    novelurl = scrapy.Field()
    category = scrapy.Field()
    nameid = scrapy.Field()
    novelnumber = scrapy.Field()
    author = scrapy.Field()
class DcontentItem(scrapy.Item):
    id_name = scrapy.Field()
    chaptercontent = scrapy.Field()
    num = scrapy.Field()
    url = scrapy.Field()
    chaptername = scrapy.Field()
