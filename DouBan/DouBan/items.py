# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	#评分
	point=scrapy.Field()
	#描述
	description=scrapy.Field()
	#名字
	name=scrapy.Field()
	
	
