# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class TecentPipeline(object):
	def __init__(self):
		self.filename=open("job.json","w")


	def process_item(self, item, spider):
		text=json.dumps(dict(item),ensure_ascii=False)
		self.filename.write(text)
		return item
