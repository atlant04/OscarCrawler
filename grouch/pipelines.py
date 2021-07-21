from io import TextIOWrapper
from itemadapter import ItemAdapter
import json 
from pymongo import MongoClient

class MongoPipeline:

    collection_name = 'scrapy_items'
    file: TextIOWrapper
    client: MongoClient

    def process_item(self, item, spider):
        dict = ItemAdapter(item).asdict()
        self.client.test[spider.term].insert_one(dict)

    def open_spider(self, spider):
        self.file = open('data.json', 'w')
        self.client = MongoClient("mongodb+srv://admin:PiYWWa0lNbvv8yVv@oscar.ima5l.mongodb.net/Oscar?retryWrites=true&w=majority")

    def close_spider(self, spider):
        self.file.close()