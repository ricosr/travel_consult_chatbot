# -*- coding:utf-8 -*-

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["travel"]
mycol = mydb["food"]


def search_loc(loc):
    return {"$or": [{"详细地址": {"$regex": ".*" + loc + ".*"}},{"所属片区":{"$regex": ".*" + loc + ".*"}}]}


def search_food(food):
    return {"$or": [{"特色菜": {"$regex": ".*" + food + ".*"}},{"类别":{"$regex": ".*" + food + ".*"}}]}


def search_rest(rest):
    return {"$or": [{"店铺名称": {"$regex": ".*" + rest + ".*"}}]}


def based_on_food(sent):
    myquery = search_food(sent)
    mydoc = mycol.find(myquery,limit=5, sort=[("评分",pymongo.DESCENDING)])
    result = [x for x in mydoc]
    return result
# print(based_on_food("小龙虾"))


def based_on_rest(sent):
    # myquery = {"$or": [{"店铺名称": {"$regex": ".*" + sent + ".*"}}]}
    myquery = search_rest(sent)
    mydoc = mycol.find(myquery,limit=5, sort=[("评分",pymongo.DESCENDING)])
    result = [x for x in mydoc]
    return result
# based_on_rest("全聚德")


def based_on_rest_food(rest,food):
    myquery = {"$and": [search_rest(rest),search_food(food)]}
    mydoc = mycol.find(myquery,limit=5, sort=[("评分",pymongo.DESCENDING)])
    result = [x for x in mydoc]
    return result
# based_on_rest_food("全聚德","烤鸡")


def based_on_loc_food(loc,food):
    myquery = {"$and":[search_loc(loc),search_food(food)]}
    mydoc = mycol.find(myquery,limit=5, sort=[("评分",pymongo.DESCENDING)])
    result = [x for x in mydoc]
    return result
# based_on_loc_food("朝阳","羊肉")


def based_on_loc_rest(loc,rest):
    myquery = {"$and":[search_loc(loc),search_rest(rest)]}
    mydoc = mycol.find(myquery,limit=5, sort=[("评分",pymongo.DESCENDING)])
    result = [x for x in mydoc]
    return result
# based_on_loc_rest("朝阳","全聚德")


def based_on_loc_rest_food(loc,rest,food):
    myquery = {"$and":[search_loc(loc),search_rest(rest),search_food(food)]}
    mydoc = mycol.find(myquery,limit=5, sort=[("评分",pymongo.DESCENDING)])
    result = [x for x in mydoc]
    return result
#based_on_loc_rest_food("朝阳","全聚德","鸭脖")


def classify(query_dic):
    if "food" in query_dic and "restaurant" in query_dic and "location" in query_dic:
        return based_on_loc_rest_food(query_dic["location"],query_dic["restaurant"],query_dic["food"])
    elif "food" in query_dic and "restaurant" in query_dic:
        return based_on_rest_food(query_dic["restaurant"],query_dic["food"])
    elif "food" in query_dic and "location" in query_dic:
        return based_on_loc_food(query_dic["location"], query_dic["food"])
    elif "location" in query_dic and "restaurant" in query_dic:
        return based_on_loc_rest(query_dic["location"],query_dic["restaurant"])
    elif "food" in query_dic:
        return based_on_food(query_dic["food"])
    elif "restaurant" in query_dic:
        return based_on_rest(query_dic["restaurant"])
    else:
        return None
