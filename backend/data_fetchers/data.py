import pymongo
from os import environ


class DB:
    DB_NAME = 'azpricetrack'
    CONNECTION_STRING_PATH = '../secrets/mongo_connection.txt'
    ITEM_COLLECTION_NAME = 'item'
    PRICE_COLLECTION_NAME = 'price'
    __db = None

    @staticmethod
    def get_db():
        if not DB.__db:
            conn_str = environ["PRICE_FETCHER_MONGO_CONNECTION"]
            mongo_client = pymongo.MongoClient(conn_str)
            DB.__db = mongo_client[DB.DB_NAME]
        return DB.__db

    @staticmethod
    def add_items(items):
        db = DB.get_db()
        collection = db[DB.ITEM_COLLECTION_NAME]
        for item in items:
            collection.insert_one(item)

    @staticmethod
    def remove_items(query):
        db = DB.get_db()
        collection = db[DB.ITEM_COLLECTION_NAME]
        collection.delete_many(query)

    @staticmethod
    def get_items():
        db = DB.get_db()
        collection = db[DB.ITEM_COLLECTION_NAME]
        return [doc for doc in collection.find({})]

    @staticmethod
    def save_price(price):
        db = DB.get_db()
        collection = db[DB.PRICE_COLLECTION_NAME]
        collection.insert_one(price)

if __name__ == '__main__':
    #DB.add_items([{'fetcher_name':'amazon', 'url':'https://www.amazon.com/dp/B01FOHJAY0?aaxitk=Zjo6TKFu.6I7aMNex51ZoQ&pd_rd_i=B01FOHJAY0&pf_rd_p=9420597b-7dad-4cbd-a28d-7d676ac67378&hsa_cr_id=3555886890201&sb-ci-n=asinImage&sb-ci-v=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F61QgIdENkhL.jpg&sb-ci-a=B01FOHJAY0'}])
    #DB.add_items([{'fetcher_name':'amazon', 'url':'https://www.amazon.com/dp/B01FOHJAY0?aaxitk=Zjo6TKFu.6I7aMNex51ZoQ&pd_rd_i=B01FOHJAY0&pf_rd_p=9420597b-7dad-4cbd-a28d-7d676ac67378&hsa_cr_id=3555886890201&sb-ci-n=asinImage&sb-ci-v=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F61QgIdENkhL.jpg&sb-ci-a=B01FOHJAY0'}])
    DB.remove_items({})
    DB.add_items([
        {'fetcherName':'amazon', 'host':'www.amazon.com', 'itemId':'B01FOHJAY0'},
        {'fetcherName':'amazon', 'host':'www.amazon.com', 'itemId':'B07CJ3CYF7'},
        {'fetcherName':'amazon', 'host':'www.amazon.com', 'itemId':'B06WWQ7KLV'},
        {'fetcherName':'amazon', 'host':'www.amazon.com', 'itemId':'B079JD7F7G'},
        {'fetcherName':'amazon', 'host':'www.amazon.com', 'itemId':'B07FJWLLDB'}
     ])
    print(DB.get_items())