# -*- coding: utf-8 -*-

# from config.config import database_address, database_name

# import copy
import pymongo


class Database:
    def __init__(self, database_address, database_name):
        self.database_address = database_address
        self.database_name = database_name
        self.db_conn = self.connect_db()

    def connect_db(self):
        client = pymongo.MongoClient(self.database_address)
        return client[self.database_name]

    def get_db_conn(self):
        return self.db_conn

    def write_db(self, dict_obj, collection_name):
        posts = self.db_conn[collection_name]
        posts.insert(dict_obj)

    def search_db(self, collection_name, query_dict):
        collection_obj = self.db_conn[collection_name]
        query_result = collection_obj.find(query_dict)
        return list(query_result)

# db_conn = Database("mongodb://super_sr:123456@209.97.166.185:27017/admin", "Travel_DB")
# db_conn.write_db({"restaurant": "kfc", "food": "hamburger", "area": "near", "price": "cheap"}, "restaurant")
# db_conn.write_db({"restaurant": "kfc", "food": "hamburger", "area": "far", "price": "cheap"}, "restaurant")

# db_conn.write_db({"restaurant": "yoshinoya", "food": "rice", "area": "far", "price": "cheap"}, "restaurant")
# db_conn.write_db({"restaurant": "abcd", "food": "hotpot", "area": "near", "price": "expensive"}, "restaurant")
# print(db_conn.search_db("restaurant", {"restaurant":"kfc"}))





# TODO: run it independently in the future

