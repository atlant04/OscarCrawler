from io import TextIOWrapper
from itemadapter import ItemAdapter
import json 
import os
from pymongo import MongoClient
from decouple import config

class MongoPipeline:

    collection_name = 'scrapy_items'
    file: TextIOWrapper
    client: MongoClient

    def process_item(self, item, spider):
        dict = ItemAdapter(item).asdict()
        self.client.test[spider.term].insert_one(dict)

    def open_spider(self, spider):
        mongo_pass = config("MONGODB_PASS")
        self.file = open('data.json', 'w')
        self.client = MongoClient(f'mongodb+srv://admin:{mongo_pass}@oscar.ima5l.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

    def close_spider(self, spider):
        self.file.close()