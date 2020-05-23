from spiderfind.items import PostItem
from spiderfind.items import contentItem
import scrapy
import time

class SpiderTitleFind(scrapy.Spider):
	name = 'titlefind'
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
				yield item

			except IndexError:
				pass

			continue
