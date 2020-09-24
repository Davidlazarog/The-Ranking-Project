from pymongo import MongoClient
from src.config import DBURL

client = MongoClient(DBURL)
db = client.get_database()