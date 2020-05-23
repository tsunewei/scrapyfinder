# -*- coding: utf-8 -*-
from spiderfind.items import AmStockItem 
import scrapy
import time
import io

class AmStockFind(scrapy.Spider):
	name = 'amstock'
	allowed_domains = ['tw.stock.yahoo.com']
	start_urls = ['https://tw.stock.yahoo.com/us/s/kimo_listUS2.html?rr=15885955562240.9866762379848004']

	def parse(self, response):
		url = 'https://tw.stock.yahoo.com/us/s/kimo_listUS2.html?rr=15885955562240.9866762379848004'
		current_url = response.url
		body = response.body 

		yield scrapy.Request (url, callback=self.parse_article)


	def parse_article(self, response):
		item = AmStockItem()
	
		target = response.xpath('//td/a/@href').extract()
		#target = response.xpath('//td/a/@href').extract()
		#target = response.xpath('//td/font/text()').extract()
		#word = response.xpath('//td/b/text()').extract() 
		#href = response.xpath('//td/a/text()').extract() 

		self.fileWrite(target)	

	def fileWrite(self, target):
		sFile = io.open('output/amstock.txt', 'w', encoding = 'UTF-8')

		for urldata in target:
			urlbreak = urldata+"\n"
			sFile.writelines(urlbreak)

		sFile.close()	
