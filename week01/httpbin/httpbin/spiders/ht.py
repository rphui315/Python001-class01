import scrapy


class HtSpider(scrapy.Spider):
    name = 'ht'
    allowed_domains = ['httpbin.org/']
    #通过IP查看请求IP
    #start_urls = ['http://httpbin.org/ip']
    #通过header查看user_agent
    start_urls = ['http://httpbin.org/headers']

    def parse(self, response):
        #pass
        print(response.text)
