# -*- coding: utf-8 -*-

import json
from urllib.request import urlopen, quote

from request_api.api_config import baidu_map_ak as ak


def get_lng_lat(address):
    url = 'http://api.map.baidu.com/geocoding/v3/?address={}&output=json&ak={}&callback=showLocation'.format(quote(address), ak)
    req = urlopen(url)
    res = req.read().decode()
    temp = json.loads(res[27:-1])
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    return lat, lng  # 纬度 latitude   ，   经度 longitude  ，


def get_bus_route(o1, o2, d1, d2):
    url = "http://api.map.baidu.com/directionlite/v1/transit?origin={},{}&destination={},{}&ak={}".format(o1, o2, d1, d2, ak)
    req = urlopen(url)
    response = req.read().decode()
    result_dict = json.loads(response)
    oute_result_dict = {}
    for index in range(len(result_dict["result"]["routes"])):
        tmp_route = ''
        for each_step in result_dict["result"]["routes"][index]["steps"]:
            tmp_route += each_step[0]["instruction"] + "-->"
        oute_result_dict[index] = tmp_route + "到达目的地"
    return oute_result_dict


def get_walk_route(o1, o2, d1, d2):
    url = "http://api.map.baidu.com/directionlite/v1/walking?origin={},{}&destination={},{}&ak={}".format(o1, o2, d1, d2, ak)
    req = urlopen(url)
    response = req.read().decode()
    result_dict = json.loads(response)
    route_result_dict = {}
    temp_route = ''
    # print(result_dict["result"]["routes"])
    for each_step in result_dict["result"]["routes"][0]["steps"]:
        temp_route += each_step["instruction"] + ','
    route_result_dict[0] = temp_route.replace("<b>", '').replace("</b>", '') + "到达目的地"
    return route_result_dict


def get_ride_route(o1, o2, d1, d2):
    url = "http://api.map.baidu.com/directionlite/v1/riding?origin={},{}&destination={},{}&ak={}".format(o1, o2, d1, d2, ak)
    req = urlopen(url)
    response = req.read().decode()
    result_dict = json.loads(response)
    route_result_dict = {}
    temp_route = ''
    # print(result_dict["result"]["routes"])
    for each_step in result_dict["result"]["routes"][0]["steps"]:
        if "turn_type" in each_step:
            temp_route += each_step["turn_type"] + each_step["instruction"] + ','
        else:
            temp_route += each_step["instruction"] + ','
    route_result_dict[0] = temp_route.replace("<b>", '').replace("</b>", '').replace("无效", '') + "到达目的地"
    return route_result_dict


def get_drive_route(o1, o2, d1, d2):
    url = "http://api.map.baidu.com/directionlite/v1/driving?origin={},{}&destination={},{}&ak={}".format(o1, o2, d1, d2, ak)
    req = urlopen(url)
    response = req.read().decode()
    result_dict = json.loads(response)
    route_result_dict = {}
    temp_route = ''
    for each_step in result_dict["result"]["routes"][0]["steps"]:
        temp_route += each_step["instruction"] + ','
    route_result_dict[0] = temp_route.replace("<b>", '').replace("</b>", '').replace("无效", '') + "到达目的地"
    return route_result_dict


def get_traffic_route_interface(search_para_dict):
    try:
        destination = search_para_dict["departure"]
        departure = search_para_dict["destination"]
        vehicle = search_para_dict["vehicle"]
        o = get_lng_lat(destination)
        d = get_lng_lat(departure)
        if vehicle in ["打车", "驾车", "摩托车"]:
            return get_drive_route(o[0], o[1], d[0], d[1])
        elif vehicle in ["公交", "客车"]:
            return get_bus_route(o[0], o[1], d[0], d[1])
        elif vehicle == "步行":
            return get_walk_route(o[0], o[1], d[0], d[1])
        elif vehicle == "骑行":
            return get_ride_route(o[0], o[1], d[0], d[1])
        else:
            return {0: "抱歉，这个路线我查不到"}
    except Exception as e:
        return {0: "抱歉，这个路线我查不到"}

