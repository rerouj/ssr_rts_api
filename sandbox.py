from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017/')

db = mongo_client['test_apirts']
collection = db["show_test"]