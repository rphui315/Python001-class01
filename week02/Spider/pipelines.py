# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.exceptions import DropItem
 
 
class MysqlPipeline(object):
	
	"""
	同步操作
	"""

	def __init__(self):
		# 建立连接
		self.conn = pymysql.connect(host = "47.94.****",user = "root",passwd = "*******",db = "movies",port = 3306,charset = 'utf8')  # 有中文要存入数据库的话要加charset='utf8'
		# 创建游标
		self.cursor = self.conn.cursor()
	
	def process_item(self,item,spider):
		
		insert_sql = 'replace into maoyan(title,link,mole,time,score) VALUES(%s,%s,%s,%s,%s)'
		try:
			self.cursor.execute(insert_sql,(item['title'],item['link'],item['mole'],item['time'],item['score']))
			print(f"title={item['title']}")
			
			 
			self.conn.commit()
		except Exception as e:
			print ('error========',e)
	

 
	def close_spider(self,spider):
		# 关闭游标和连接
		self.cursor.close()
		self.conn.close()

'''

import pymysql
dbInfo = {
    'host' : '',
    'port' : 3306,
    'user' : '',
    'password' : '',
    'db' : ''
}

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 注册到settings.py文件的ITEM_PIPELINES中，激活组件
class MaoyanmoviePipeline:
#    def process_item(self, item, spider):
#        return item

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
     def process_item(self, item, spider):
         movie_name = item['movie_name']
         movie_type = item['movie_type']
         movie_time = item['movie_time']
         #output = f'|{movie_name}|\t|{movie_type}|\t|{movie_time}|\n\n'
         #with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as article:
             #article.write(output)
             #article.close()
         conn = pymysql.connect(
            host = dbInfo['host'],
            port = dbInfo['port'],
            user = dbInfo['user'],
            password = dbInfo['password'],
            db = dbInfo['db']
         )
        # 游标建立的时候就开启了一个隐形的事务
         cur = conn.cursor()
         try:
             values = [movie_name,movie_type, movie_time]
             print(values)
             cur.execute('INSERT INTO  tb2 values(%s,%s,%s)' ,values)
             # 关闭游标
             cur.close()
             conn.commit()
         except:
             conn.rollback()
        # 关闭数据库连接
         conn.close()

         return item
'''