# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd

class SpiderPipeline:
	def process_item(self, item, spider):
		title = item['title']
		link = item['link']
		mole = item['mole']
		time = item['time']
		score = item['score']

		df = pd.DataFrame([{'title':title,"link":link,"mole":mole,"time":time,"score":score}])
	

		df.to_csv('/Users/renpenghui/Python001-class01/week01/Spider/Spider/homework02.csv',encoding='utf_8_sig',index=False,mode="a",header=False)
		return item 