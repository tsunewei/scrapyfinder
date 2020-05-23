from spiderfind.items import PostItem
from spiderfind.items import contentItem
import scrapy
import time

class SpiderContentFind(scrapy.Spider):
	name = 'contentfind'
	allowed_domains = ['ptt.cc']
	start_urls = ['https://www.ptt.cc/bbs/Baseball/index.html']

	def parse(self, response):
		url = 'https://www.ptt.cc/bbs/Baseball/index.html'
		current_url = response.url
		body = response.body 
	
		yield scrapy.Request (url, callback=self.parse_article)

	def parse_article(self, response):
		item = PostItem()
		target = response.css("div.r-ent")

		for tag in target:
			try:
				item['title'] = tag.css("div.title a::text")[0].extract()
				item['author'] = tag.css('div.author::text')[0].extract()
				item['date'] = tag.css('div.date::text')[0].extract()
				item['push'] = tag.css('span::text')[0].extract()
				item['url'] = tag.css('div.title a::attr(href)')[0].extract()

				url = 'https://www.ptt.cc'+item['url']
				#yield item
				yield scrapy.Request (url, callback=self.parse_content)

			except IndexError:
				pass

			continue

	def parse_content(self, response):
		item = contentItem()
		target = response.css("title")			
		
		for tag in target:
			try:
				#item['title'] = response.css('title::text')[0].extract() 
				item['title'] = response.xpath('//meta[@property="og:title"]/@content')[0].extract() 
				item['content'] = response.xpath('//meta[@property="og:description"]/@content')[0].extract() 
				print "==>"+item['title']+","+item['content']

				yield item
			except IndexError:
				pass

