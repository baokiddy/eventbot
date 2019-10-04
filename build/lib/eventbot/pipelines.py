# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class EventbotPipeline(object):
#     def process_item(self, item, spider):
#         return item

import pymongo
import logging

class ApiPipeline(object):

    collection_name = 'eventbrite_4'

    def __init__(self, api_endpoint, api_key):
        self.api_endpoint = api_endpoint
        self.api_key = api_key

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            api_endpoint=crawler.settings.get('API_ENDPOINT'),
            api_key=crawler.settings.get('API_KEY')
        )

    def open_spider(self, spider):
        ## initializing spider
        ## opening db connection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        ## clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        ## how to handle each post
        self.db[self.collection_name].insert(dict(item))
        logging.debug("Post added to MongoDB")
        return item


class MongoDBPipeline(object):

    # def __init__(self):
    #     connection = pymongo.MongoClient(
    #         Settings['MONGODB_SERVER'],
    #         Settings['MONGODB_PORT']
    #     )
    #     db = connection[Settings['MONGODB_DB']]
    #     self.collection = db[Settings['MONGODB_COLLECTION']]

    # def process_item(self, item, spider):
    #         valid = True
    #         for data in item:
    #             if not data:
    #                 valid = False
    #                 raise DropItem("Missing {0}!".format(data))
    #         if valid:
    #             self.collection.insert(dict(item))
    #             logging.msg("Event added to MongoDB database!",
    #                     level=log.DEBUG, spider=spider)
    #         return item

    collection_name = 'eventbrite_5'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        ## initializing spider
        ## opening db connection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        ## clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        ## how to handle each post
        self.db[self.collection_name].insert(dict(item))
        logging.debug("Post added to MongoDB")
        return item