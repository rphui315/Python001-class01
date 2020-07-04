# -*- coding: utf-8 -*-

# Scrapy settings for Spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Spider'

SPIDER_MODULES = ['Spider.spiders']
NEWSPIDER_MODULE = 'Spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
# RANDOM_UA_TYPE = "random"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
'host':'maoyan.com',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Cookie':'uuid_n_v=v1; uuid=E9BA41F0B45111EAACB6BBD781D89938DF0B59FCC2E048AAA8CF7B842C9288D9; mojo-uuid=2732764aa91bb3b1219b9cf973f2924f; _lxsdk_cuid=172dab90d42c8-063f78b6e46902-31607402-1ea000-172dab90d42c8; _lxsdk=E9BA41F0B45111EAACB6BBD781D89938DF0B59FCC2E048AAA8CF7B842C9288D9; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _csrf=64706eaff01f10d32e7120aad0d6c73a54d8c0ed06bbc1a24b0f467610336b8c; mojo-session-id={"id":"22198546e2722589b02de9ad0c2c2cf4","time":1592835639039}; mojo-trace-id=1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592809900,1592809935,1592810323,1592835639; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592835639; __mta=217993513.1592807462213.1592812014078.1592835639266.12; _lxsdk_s=172dc670713-90c-8f9-313%7C%7C3'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {

#  

#    'Spider.middlewares.SpiderSpiderMiddleware': 543,
# }
DELTAFETCH_ENABLED = True
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {


# 'Spider.middlewares.RandomUserAgentMiddleware':543, 
# 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
'Spider.middlewares.RandomHttpProxyMiddleware': 400,
}


HTTP_PROXY_LIST = [
     'http://207.180.215.74:3128',
     'http://118.69.50.154:443',
     'http://110.37.231.92:8080',
]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Spider.pipelines.MysqlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
