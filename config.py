from pymongo import MongoClient
from settings import MONGO_URL


mongo = MongoClient(MONGO_URL)