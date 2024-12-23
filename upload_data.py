from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
url = "mongodb+srv://dushyant_braintumor:Dushyant12@cluster0.rzlrf.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connect to the server
client = MongoClient(url)

#create database name and collection name
DATABASE_NAME = "Dushyant_brain"
COLLECTION_NAME = "BrainTumor"