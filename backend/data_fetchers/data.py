import pymongo
from os import path

class DB:
    DB_NAME = 'azpricetrack'
    CONNECTION_STRING_PATH = '../secrets/mongo_connection.txt'
    ITEM_COLLECTION_NAME = 'item'
    __db = None

    @staticmethod
    def get_db():
        if not DB.__db:
            conn_str = None
            if path.exists(DB.CONNECTION_STRING_PATH):
                with open(DB.CONNECTION_STRING_PATH) as f:
                    conn_str = f.read()
            mongo_client = pymongo.MongoClient(conn_str)
            DB.__db = mongo_client[DB.DB_NAME]
        return DB.__db
    @staticmethod
    def add_items(items):
        db = DB.get_db()
        db[DB.ITEM_COLLECTION_NAME].insert_many(items)

if __name__ == '__main__':
    DB.add_items([{'fetcher_name':'amazon', 'url':'https://www.amazon.com/dp/B01FOHJAY0?aaxitk=Zjo6TKFu.6I7aMNex51ZoQ&pd_rd_i=B01FOHJAY0&pf_rd_p=9420597b-7dad-4cbd-a28d-7d676ac67378&hsa_cr_id=3555886890201&sb-ci-n=asinImage&sb-ci-v=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F61QgIdENkhL.jpg&sb-ci-a=B01FOHJAY0'}])
