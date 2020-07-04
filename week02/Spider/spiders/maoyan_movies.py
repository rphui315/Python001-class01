# -*- coding: utf-8 -*-
import scrapy
from Spider.items import SpiderItem
from scrapy.selector import Selector


class MaoyanMoviesSpider(scrapy.Spider):
	name = 'maoyan_movies'
	allowed_domains = ['maoyan.com']
	# start_urls = ['http://maoyan.com/']
	def start_requests(self):
		urls = [f'https://maoyan.com/films?showType=3&offset={i*30}' for i in range(0,10)]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)





	def parse(self, response):
		# print(response.url) 打印网页地址
		# print(response.text) #打印内容

		movies = Selector(response=response).xpath("//dd")

		for i in movies:
			item = SpiderItem()
			title =  i.xpath("./div[@class='channel-detail movie-item-title']/a/text()").get()
			link = "https://maoyan.com"+i.xpath("./div[@class='channel-detail movie-item-title']/a/@href").get()
			if i.xpath('./div[@class="channel-detail channel-detail-orange"]/text()').get() == "暂无评分":
				score = "暂无评分"
			else:
				score = i.xpath('./div/i/text()').getall()[0]+i.xpath('./div/i/text()').getall()[1]
			


			item['score'] = score
			item["title"] = title
			item["link"] = link
			yield scrapy.Request(url=link,meta={'item':item},callback=self.parse2)
	
	def parse2(self,response):
		item = response.meta["item"]
		tags = Selector(response=response).xpath("//div[@class='movie-brief-container']")
		molelist = tags.xpath("./ul/li/a/text()").getall()
		mole = ""
		for i in molelist:
			mole+=i+"/"
		item['mole'] = mole
		time = tags.xpath("./ul/li[@class='ellipsis'][3]/text()").get()[:10]
		item['time'] = time
		yield item



		

