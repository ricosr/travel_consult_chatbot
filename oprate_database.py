# -*- coding: utf-8 -*-

# from config.config import database_address, database_name

import pymongo


class Database:
    def __init__(self, database_address, database_name):
        self.database_address = database_address
        self.database_name = database_name

    def connect_db(self):
        client = pymongo.MongoClient(self.database_address)
        db_opt = client[self.database_name]
        return db_opt

    def write_db(self, dict_obj, collection_name, db_opt):
        posts = db_opt[collection_name]
        posts.insert(dict_obj)

    def read_db(self, db_opt, collection_name, query_dict):
        collection_obj = db_opt[collection_name]
        query_result = collection_obj.find(query_dict)
        return query_result

# TODO: run it independently in the future
