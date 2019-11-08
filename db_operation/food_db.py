# -*- coding:utf-8 -*-

import pymongo

LIMIT_NO = 5

SHOW_ITEM = ['店铺名称', '类别', '评分', '详细地址', '营业时间', '联系电话']


def search_loc(loc):
    return {"$or": [{"详细地址": {"$regex": ".*" + loc + ".*"}}, {"所属片区": {"$regex": ".*" + loc + ".*"}}]}


def search_food(food):
    return {"$or": [{"特色菜": {"$regex": ".*" + food + ".*"}}, {"类别": {"$regex": ".*" + food + ".*"}}]}


def search_rest(rest):
    return {"$or": [{"店铺名称": {"$regex": ".*" + rest + ".*"}}]}


def based_on_food(sent, mycol):
    myquery = search_food(sent)
    mydoc = mycol.find(myquery, limit=LIMIT_NO, sort=[("评分", pymongo.DESCENDING)])
    result_ls = []
    for each_res in mydoc:
        tmp_dict = {}
        for key, val in each_res.items():
            if key in SHOW_ITEM:
                tmp_dict[key] = val
        result_ls.append(tmp_dict)
    return result_ls
    # result = [x for x in mydoc]
    # return result
# print(based_on_food("小龙虾"))


def based_on_rest(sent, mycol):
    # myquery = {"$or": [{"店铺名称": {"$regex": ".*" + sent + ".*"}}]}
    myquery = search_rest(sent)
    mydoc = mycol.find(myquery, limit=LIMIT_NO, sort=[("评分", pymongo.DESCENDING)])
    result_ls = []
    for each_res in mydoc:
        tmp_dict = {}
        for key, val in each_res.items():
            if key in SHOW_ITEM:
                tmp_dict[key] = val
        result_ls.append(tmp_dict)
    return result_ls
    # return result
# based_on_rest("全聚德")


def based_on_rest_food(rest, food, mycol):
    myquery = {"$and": [search_rest(rest), search_food(food)]}
    mydoc = mycol.find(myquery, limit=LIMIT_NO, sort=[("评分", pymongo.DESCENDING)])
    result_ls = []
    for each_res in mydoc:
        tmp_dict = {}
        for key, val in each_res.items():
            if key in SHOW_ITEM:
                tmp_dict[key] = val
        result_ls.append(tmp_dict)
    return result_ls
    # result = [x for x in mydoc]
    # return result
# based_on_rest_food("全聚德","烤鸡")


def based_on_loc_food(loc, food, mycol):
    myquery = {"$and": [search_loc(loc), search_food(food)]}
    mydoc = mycol.find(myquery, limit=LIMIT_NO, sort=[("评分", pymongo.DESCENDING)])
    result_ls = []
    for each_res in mydoc:
        tmp_dict = {}
        for key, val in each_res.items():
            if key in SHOW_ITEM:
                tmp_dict[key] = val
        result_ls.append(tmp_dict)
    return result_ls
    # result = [x for x in mydoc]
    # return result
# based_on_loc_food("朝阳","羊肉")


def based_on_loc_rest(loc, rest, mycol):
    myquery = {"$and": [search_loc(loc), search_rest(rest)]}
    mydoc = mycol.find(myquery, limit=LIMIT_NO, sort=[("评分", pymongo.DESCENDING)])
    result_ls = []
    for each_res in mydoc:
        tmp_dict = {}
        for key, val in each_res.items():
            if key in SHOW_ITEM:
                tmp_dict[key] = val
        result_ls.append(tmp_dict)
    return result_ls
    # result = [x for x in mydoc]
    # return result
# based_on_loc_rest("朝阳","全聚德")


def based_on_loc_rest_food(loc, rest, food, mycol):
    myquery = {"$and": [search_loc(loc), search_rest(rest), search_food(food)]}
    mydoc = mycol.find(myquery, limit=LIMIT_NO, sort=[("评分", pymongo.DESCENDING)])
    result_ls = []
    for each_res in mydoc:
        tmp_dict = {}
        for key, val in each_res.items():
            if key in SHOW_ITEM:
                tmp_dict[key] = val
        result_ls.append(tmp_dict)
    return result_ls
    # result = [x for x in mydoc]
    # return result
# based_on_loc_rest_food("朝阳","全聚德","鸭脖")


def search_consult_food(query_dic, mycol):
    if "food" in query_dic and "restaurant" in query_dic and "location" in query_dic:
        result = based_on_loc_rest_food(query_dic["location"], query_dic["restaurant"], query_dic["food"], mycol)
        if not result:
            result = based_on_rest_food(query_dic["restaurant"], query_dic["food"], mycol)
            if not result:
                result1 = based_on_food(query_dic["food"], mycol)
                if result1:
                    return result1
                result2 = based_on_rest(query_dic["restaurant"], mycol)
                if result2:
                    return result2
            else:
                return result
        else:
            return result
    elif "food" in query_dic and "restaurant" in query_dic:
        result = based_on_rest_food(query_dic["restaurant"], query_dic["food"], mycol)
        if result:
            return result
        else:
            result1 = based_on_food(query_dic["food"], mycol)
            if result1:
                return result1
            result2 = based_on_rest(query_dic["restaurant"], mycol)
            if result2:
                return result2
    elif "food" in query_dic and "location" in query_dic:
        result = based_on_loc_food(query_dic["location"], query_dic["food"], mycol)
        if result:
            return result
        else:
            result = based_on_food(query_dic["food"], mycol)
            if result:
                return result
    elif "location" in query_dic and "restaurant" in query_dic:
        result = based_on_loc_rest(query_dic["location"], query_dic["restaurant"], mycol)
        if result:
            return result
        else:
            result = based_on_rest(query_dic["restaurant"], mycol)
            if result:
                return result
    elif "food" in query_dic:
        result = based_on_food(query_dic["food"], mycol)
        if result:
            return result
    elif "restaurant" in query_dic:
        result = based_on_rest(query_dic["restaurant"], mycol)
        if result:
            return result
    else:
        return None


