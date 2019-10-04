# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EventbotItem(scrapy.Item):
    # define the fields for your item here like:
    event_name = scrapy.Field()
    event_link = scrapy.Field()
    event_date = scrapy.Field()
    event_location = scrapy.Field()
    event_price = scrapy.Field()
    
