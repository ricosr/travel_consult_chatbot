# -*- coding: utf-8 -*-

import random

airports = {
    "北京": ["北京首都国际机场", "北京大兴国际机场"],
    "上海": ["上海虹桥国际机场", "上海浦东国际机场"],
    "天津": ["天津滨海国际机场"],
    "重庆": ["重庆江北国际机场"],
    "万州": ["万州五桥机场"],
    "黔江": ["黔江武陵山机场"],
    "武隆": ["武隆仙女山机场"],
    "石家庄": ["石家庄正定国际机场"],
    "秦皇岛": ["秦皇岛北戴河国际机场"],
    "邯郸": ["邯郸机场"],
    "唐山": ["唐山三女河机场"],
    "张家口": ["张家口宁远机场"],
    "太原": ["太原武宿国际机场"],
    "长治": ["长治王村机场"],
    "大同": ["大同云冈机场"],
    "运城": ["运城关公机场"],
    "吕梁": ["吕梁大武机场"],
    "临汾": ["临汾乔李机场"],
    "忻州": ["忻州五台山机场"],
    "呼和浩特": ["呼和浩特白塔国际机场"],
    "呼伦贝尔": ["呼伦贝尔东山国际机场"],
    "鄂尔多斯": ["鄂尔多斯伊金霍洛国际机场"],
    "满洲里": ["满洲里西郊国际机场"],
    "二连浩特": ["二连浩特赛乌苏国际机场"],
    "赤峰": ["赤峰玉龙机场"],
    "包头": ["包头东河机场"],
    "通辽": ["通辽机场"],
    "乌兰察布": ["乌兰察布集宁机场"],
    "乌兰浩特": ["乌兰浩特机场"],
    "阿尔山": ["阿尔山伊尔施机场"],
    "巴彦淖尔": ["巴彦淖尔天吉泰机场"],
    "乌海": ["乌海机场"],
    "锡林郭勒": ["锡林浩特机场"],
    "阿拉善": ["巴彦浩特通勤机场", "巴丹吉林通勤机场"],
    "额济纳": ["额济纳旗桃来机场"],
    "沈阳": ["沈阳桃仙国际机场"],
    "大连": ["大连周水子国际机场"],
    "丹东": ["丹东浪头国际机场"],
    "锦州": ["锦州小岭子机场"],
    "朝阳": ["朝阳机场"],
    "鞍山": ["鞍山腾鳌机场"],
    "长春": ["长春龙嘉国际机场"],
    "延吉": ["延吉朝阳川国际机场"],
    "延边": ["延吉朝阳川国际机场"],
    "白城": ["白城长安机场"],
    "白山": ["白山长白山机场"],
    "通化": ["通化三源浦机场"],
    "哈尔滨": ["哈尔滨太平国际机场"],
    "齐齐哈尔": ["齐齐哈尔三家子机场"],
    "牡丹江": ["牡丹江海浪机场"],
    "佳木斯": ["佳木斯东郊机场"],
    "大庆": ["大庆萨尔图机场"],
    "伊春": ["伊春林都机场"],
    "鸡西": ["鸡西兴凯湖机场"],
    "加格达奇": ["加格达奇嘎仙机场"],
    "黑河": ["黑河瑷珲机场"],
    "漠河": ["漠河古莲机场"],
    "建三江": ["建三江湿地机场"],
    "南京": ["南京禄口国际机场"],
    "无锡": ["苏南硕放国际机场"],
    "连云港": ["连云港白塔埠国际机场"],
    "扬州": ["扬州泰州国际机场"],
    "常州": ["常州奔牛国际机场"],
    "盐城": ["盐城南洋国际机场"],
    "徐州": ["徐州观音国际机场"],
    "南通": ["南通兴东国际机场"],
    "淮安": ["淮安涟水机场"],
    "杭州": ["杭州萧山国际机场"],
    "宁波": ["宁波栎社国际机场"],
    "温州": ["温州龙湾国际机场"],
    "义乌": ["义乌机场"],
    "舟山": ["舟山普陀山机场"],
    "衢州": ["衢州机场"],
    "台州": ["台州路桥机场"],
    "合肥": ["合肥新桥国际机场"],
    "黄山": ["黄山屯溪国际机场"],
    "阜阳": ["阜阳西关机场"],
    "安庆": ["安庆天柱山机场"],
    "池州": ["池州九华山机场"],
    "福州": ["福州长乐国际机场"],
    "厦门": ["厦门高崎国际机场"],
    "泉州": ["泉州晋江国际机场"],
    "南平市": ["南平市武夷山机场"],
    "龙岩": ["龙岩冠豸山机场"],
    "三明": ["三明沙县机场"],
    "南昌": ["南昌昌北国际机场"],
    "九江": ["九江庐山机场"],
    "景德镇": ["景德镇罗家机场"],
    "赣州": ["赣州黄金机场"],
    "井冈山": ["井冈山机场"],
    "上饶": ["上饶三清山机场"],
    "宜春": ["宜春明月山机场"],
    "济南": ["济南遥墙国际机场"],
    "青岛": ["青岛流亭国际机场"],
    "日照": ["日照山字河国际机场"],
    "烟台": ["烟台蓬莱国际机场"],
    "临沂": ["临沂沭埠岭机场"],
    "威海": ["威海大水泊国际机场"],
    "潍坊": ["潍坊南苑机场"],
    "济宁": ["济宁曲阜机场"],
    "东营": ["东营永安机场"],
    "郑州": ["郑州新郑国际机场"],
    "洛阳": ["洛阳北郊机场"],
    "南阳": ["南阳姜营机场"],
    "信阳": ["信阳明港机场"],
    "武汉": ["武汉天河国际机场"],
    "宜昌": ["宜昌三峡机场"],
    "襄阳": ["襄阳刘集机场"],
    "恩施": ["恩施许家坪机场"],
    "十堰": ["十堰武当山机场"],
    "神农架": ["神农架机场"],
    "长沙": ["长沙黄花国际机场"],
    "张家界": ["张家界荷花机场"],
    "常德": ["常德桃花源机场"],
    "衡阳": ["衡阳南岳机场"],
    "永州": ["永州零陵机场"],
    "怀化": ["怀化芷江机场"],
    "邵阳": ["邵阳武冈机场"],
    "广州": ["广州白云国际机场"],
    "深圳": ["深圳宝安国际机场"],
    "珠海": ["珠海金湾国际机场"],
    "揭阳": ["揭阳潮汕国际机场"],
    "佛山": ["佛山沙堤机场"],
    "惠州": ["惠州平潭机场"],
    "梅州": ["梅州梅县机场"],
    "湛江": ["湛江西厅机场"],
    "汕头": ["汕头外砂机场"],
    "南宁": ["南宁吴圩国际机场"],
    "桂林": ["桂林两江国际机场"],
    "柳州": ["柳州白莲机场"],
    "北海": ["北海福成机场"],
    "梧州": ["梧州长洲岛机场"],
    "百色": ["百色巴马机场"],
    "河池": ["河池金城江机场"],
    "海口": ["海口美兰国际机场"],
    "三亚": ["三亚凤凰国际机场"],
    "琼海": ["琼海博鳌国际机场"],
    "成都": ["成都双流国际机场"],
    "绵阳": ["绵阳南郊机场"],
    "泸州": ["泸州云龙机场"],
    "宜宾": ["宜宾菜坝机场"],
    "广元": ["广元盘龙机场"],
    "九寨沟": ["九寨沟黄龙机场"],
    "南充": ["南充高坪机场"],
    "达州": ["达州河市机场"],
    "攀枝花": ["攀枝花保安营机场"],
    "康定": ["康定机场"],
    "西昌": ["西昌青山机场"],
    "稻城": ["稻城亚丁机场"],
    "贵阳": ["贵阳龙洞堡国际机场"],
    "铜仁": ["铜仁凤凰机场"],
    "黎平": ["黎平机场"],
    "荔波": ["荔波机场"],
    "兴义": ["兴义万峰林机场"],
    "安顺": ["安顺黄果树机场"],
    "六盘水": ["六盘水月照机场"],
    "遵义": ["遵义新舟机场", "遵义茅台机场"],
    "黄平": ["黄平机场"],
    "昆明": ["昆明长水国际机场"],
    "丽江": ["丽江三义国际机场"],
    "景洪市": ["西双版纳嘎洒国际机场"],
    "香格里拉": ["迪庆香格里拉机场"],
    "大理": ["大理机场"],
    "昭通": ["昭通机场"],
    "普洱": ["普洱思茅机场"],
    "保山": ["保山云瑞机场"],
    "临沧": ["临沧机场", "文山普者黑机场"],
    "腾冲": ["腾冲驼峰机场"],
    "德宏": ["德宏芒市机场"],
    "拉萨": ["拉萨贡嘎国际机场"],
    "昌都": ["昌都邦达机场"],
    "阿里": ["阿里昆莎机场"],
    "日喀则": ["日喀则和平机场"],
    "林芝": ["林芝米林机场"],
    "西安": ["西安咸阳国际机场"],
    "榆林": ["榆林西沙机场"],
    "延安": ["延安二十里铺机场", "延安南泥湾机场"],
    "兰州": ["兰州中川国际机场"],
    "敦煌": ["敦煌机场"],
    "庆阳": ["庆阳机场"],
    "嘉峪关": ["嘉峪关机场"],
    "天水": ["天水机场"],
    "甘南": ["甘南夏河机场"],
    "张掖": ["张掖甘州机场"],
    "金昌": ["金昌机场"],
    "西宁": ["西宁曹家堡国际机场"],
    "格尔木": ["格尔木机场"],
    "玉树": ["玉树巴塘机场"],
    "德令哈": ["德令哈机场"],
    "茫崖": ["花土沟机场"],
    "银川": ["银川河东国际机场"],
    "中卫": ["中卫香山机场"],
    "固原": ["固原六盘山机场"],
    "乌鲁木齐": ["乌鲁木齐地窝堡国际机场"],
    "吐鲁番": ["吐鲁番交河机场"],
    "喀什": ["喀什机场"],
    "克拉玛依": ["克拉玛依机场"],
    "石河子": ["石河子花园机场"],
    "阿勒泰": ["阿勒泰机场"],
    "塔城": ["塔城机场"],
    "博乐": ["博乐阿拉山口机场"],
    "伊宁": ["伊宁机场"],
    "哈密": ["哈密机场"],
    "库尔勒": ["库尔勒机场"],
    "温宿": ["阿克苏温宿机场"],
    "和田": ["和田机场"],
    "布尔津": ["布尔津喀纳斯机场"],
    "富蕴": ["富蕴可可托海机场"],
    "伊犁": ["那拉提机场"],
    "阿克苏": ["库车龟兹机场"],
    "巴州": ["且末玉都机场"],
    "香港": ["香港国际机场"],
    "澳门": ["澳门国际机场"],
    "台北": ["台北桃园国际机场", "台北松山机场"],
    "台中": ["台中国际机场"],
    "高雄": ["高雄小港国际机场"],
    "台南": ["台南机场"],
    "连江县": ["马祖南竿机场", "马祖北竿机场"],
    "金门": ["金门机场"]

}

airlines = ["中国南方航空", "吉祥航空", "奥凯航空", "九元航空", "长龙航空", "东方航空", "中国国际航空", "深圳航空", "海南航空",
            "春秋航空", "上海航空", "西部航空", "重庆航空", "西藏航空", "中国联合航空", "云南祥鹏航空", "厦门航空", "天津航空",
            "山东航空", "四川航空", "华夏航空", "长城航空", "成都航空", "北京首都航空"]

airlines_key = {
    "中国南方航空": "CZ",
    "吉祥航空": "HO",
    "奥凯航空": "BK",
    "九元航空": "AQ",
    "长龙航空": "GJ",
    "东方航空": "MU",
    "中国国际航空": "CA",
    "深圳航空": "ZH",
    "海南航空": "HU",
    "春秋航空": "9C",
    "上海航空": "FM",
    "西部航空": "PN",
    "重庆航空": "OQ",
    "西藏航空": "TV",
    "中国联合航空": "KN",
    "云南祥鹏航空": "8L",
    "厦门航空": "MF",
    "天津航空": "GS",
    "山东航空": "SC",
    "四川航空": "3U",
    "华夏航空": "G5",
    "长城航空": "IJ",
    "成都航空": "EU",
    "北京首都航空": "JD",
}


def make_air_ticket(departure, destination, departure_date, solution_count):
    tmp_depart_airport = ''
    tmp_dest_airport = ''
    solution_dict = {}
    ticket_template = "{departure_date}:\n{airline} {air_no}, {depart}-{depart_time} ---> {dest}-{dest_time}, ￥{fee}"
    for i in range(solution_count):
        tmp_airline = random.choice(airlines)
        tmp_airline_no = airlines_key[tmp_airline] + str(random.randint(1000,9999))
        if departure in airports:
            tmp_depart_airport = random.choice(airports[departure])
        else:
            for city, airport_ls in airports.items():
                if city in departure:
                    tmp_depart_airport = random.choice(airport_ls)
                    break
        if destination in airports:
            tmp_dest_airport = random.choice(airports[destination])
        else:
            for city, airport_ls in airports.items():
                if city in destination:
                    tmp_dest_airport = random.choice(airport_ls)
                    break
        if not tmp_depart_airport or not tmp_dest_airport:
            return False
        depart_hour = random.randint(0, 20)
        depart_min = random.randint(0, 59)
        depart_time = "{}:{}".format(depart_hour, depart_min)
        dest_hour = depart_hour + random.choice([2,3])
        dest_min = random.randint(0, 59)
        dest_time = "{}:{}".format(dest_hour, dest_min)
        tmp_fee = random.randint(500, 1800)
        solution_dict[str(i+1)] = ticket_template.format(departure_date=departure_date,airline=tmp_airline, air_no=tmp_airline_no,
                                                  depart=tmp_depart_airport, depart_time=depart_time,
                                                  dest=tmp_dest_airport, dest_time = dest_time, fee=tmp_fee)
    return solution_dict

# print(make_air_ticket("北京", "深圳", "12-12", 10))


def make_train_ticket(departure, destination, departure_date, solution_count):
    station_words = ["东站", "西站", "南站", "北站", "站"]
    train_type = ['K', 'T', 'G', 'D', 'Z']
    solution_dict = {}
    ticket_template = "出发:{departure_date}-{depart_time}, 车次:{train_no}\n{depart} ---> {dest}, 全程:{time_cost}小时, 硬座:{sit_fee}RMB, 卧铺:{lay_fee}RMB"
    for i in range(solution_count):
        departure_station = departure + random.choice(station_words)
        destination_station = destination + random.choice(station_words)
        train_no = random.choice(train_type) + str(random.randint(10, 999))
        depart_hour = random.randint(0, 20)
        depart_min = random.randint(0, 59)
        depart_time = "{}:{}".format(depart_hour, depart_min)
        time_cost = random.randint(3, 30)
        tmp_sit_fee = random.randint(100, 1000)
        tmp_lay_fee = tmp_sit_fee + 300
        solution_dict[str(i+1)] = ticket_template.format(departure_date=departure_date, depart_time=depart_time, train_no=train_no, depart=departure_station,
                                                  dest=destination_station, time_cost=time_cost, sit_fee=tmp_sit_fee, lay_fee=tmp_lay_fee)
    return solution_dict
# print(make_train_ticket("深圳", "北京", "12-12", 10))


def search_ticket_interface(search_dict, count):
    departure = search_dict["departure"]
    destination = search_dict["destination"]
    departure_date = search_dict["departure_date"]
    vehicle = search_dict["vehicle"]

    if vehicle == "飞机":
        return make_air_ticket(departure, destination, departure_date, count)
    if vehicle == "火车":
        return make_train_ticket(departure, destination, departure_date, count)
    else:
        return False






