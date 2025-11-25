from pymongo import MongoClient

"""
Get the async db connection
"""
def get_db():
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["iban-registry"]
    return db

db = get_db()