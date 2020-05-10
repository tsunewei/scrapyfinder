# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderfindItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PostItem(scrapy.Item):
	title = scrapy.Field()
	author = scrapy.Field()
	date = scrapy.Field()
	push = scrapy.Field()
	url = scrapy.Field()

class contentItem(scrapy.Item):
	title = scrapy.Field()
	content = scrapy.Field()

class AmStockItem(scrapy.Item):
	stockname = scrapy.Field() 
	time = scrapy.Field() 
	transaction = scrapy.Field() 
