# ======================================
# 1.Dictionary
# ======================================


# 宣告
# d = {key1: value1, key2: value2}
# key:value
# key是唯一的，而value不是

tinydict = {'a': 1, 'b': 2, 'c': '3'}
print(tinydict['b'])
print(tinydict)

# print(tinydict['d'])
# print(tinydict.get('d'))
# print(tinydict.keys())
# print(tinydict.values())

# print(tinydict.items())
# for key, value in tinydict.items():
#     print(key, value)


# print(tinydict.pop('a'))
# ======================================

# tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# tinydict['Age'] = 8  # 更新
# tinydict['School'] = "RUNOOB"  # 添加

# https://www.runoob.com/python/python-dictionary.html 内置函数

# ======================================
# 應用

# 每個學號對應的名子
# 每張發票編號對應的消費內容


# 每根K棒對應的價格

# {"timestamp": "1640966400", "date": "2022-01-01 00:00:00", "open": 48005.37, "high": 48027.31, "low": 47937.5,
#     "close": 48004.75, "volume": 50.29149, "closeTimestamp": "1640966460", "amount": 2413639.7779029}
# {"timestamp": "1640966460", "date": "2022-01-01 00:01:00", "open": 48007.21, "high": 48011.78, "low": 47951.5,
#     "close": 47951.5, "volume": 14.75541, "closeTimestamp": "1640966520", "amount": 708048.7543912}
# {"timestamp": "1640966520", "date": "2022-01-01 00:02:00", "open": 47956.29, "high": 47992.36, "low": 47944.49,
#     "close": 47965.46, "volume": 15.33062, "closeTimestamp": "1640966580", "amount": 735378.8514351}
# {"timestamp": "1640966580", "date": "2022-01-01 00:03:00", "open": 47965.46, "high": 47970.25, "low": 47910.56,
#     "close": 47954.34, "volume": 13.35734, "closeTimestamp": "1640966640", "amount": 640360.7683624}
# {"timestamp": "1640966640", "date": "2022-01-01 00:04:00", "open": 47954.35, "high": 47971.49, "low": 47949.55,
#     "close": 47955.58, "volume": 8.3438, "closeTimestamp": "1640966700", "amount": 400146.7485929}
# {"timestamp": "1640966700", "date": "2022-01-01 00:05:00", "open": 47955.59, "high": 47967.65, "low": 47952.29,
#     "close": 47967.65, "volume": 8.99859, "closeTimestamp": "1640966760", "amount": 431565.6302065}
# {"timestamp": "1640966760", "date": "2022-01-01 00:06:00", "open": 47967.64, "high": 47980.64, "low": 47956.26,
#     "close": 47980.03, "volume": 11.43615, "closeTimestamp": "1640966820", "amount": 548571.2417429}
# {"timestamp": "1640966820", "date": "2022-01-01 00:07:00", "open": 47980.02, "high": 47997.09, "low": 47971.66,
#     "close": 47979.62, "volume": 7.64509, "closeTimestamp": "1640966880", "amount": 366857.163216}
# {"timestamp": "1640966880", "date": "2022-01-01 00:08:00", "open": 47979.62, "high": 47990.0, "low": 47973.03,
#     "close": 47990.0, "volume": 11.34944, "closeTimestamp": "1640966940", "amount": 544574.7722498}
# {"timestamp": "1640966940", "date": "2022-01-01 00:09:00", "open": 47990.0, "high": 47999.98, "low": 47975.08,
#     "close": 47977.84, "volume": 19.1031, "closeTimestamp": "1640967000", "amount": 916789.2758295}
# {"timestamp": "1640967000", "date": "2022-01-01 00:10:00", "open": 47977.85, "high": 47987.96, "low": 47958.14,
#     "close": 47984.94, "volume": 8.65876, "closeTimestamp": "1640967060", "amount": 415439.6340091}
# {"timestamp": "1640967060", "date": "2022-01-01 00:11:00", "open": 47984.93, "high": 48040.15, "low": 47984.93,
#     "close": 48022.04, "volume": 44.71251, "closeTimestamp": "1640967120", "amount": 2147294.0569598}
# {"timestamp": "1640967120", "date": "2022-01-01 00:12:00", "open": 48022.03, "high": 48023.35, "low": 47993.97,
#     "close": 48011.74, "volume": 7.97656, "closeTimestamp": "1640967180", "amount": 382946.4302195}
# for line in BTCfile.readlines():
#     dic = json.loads(line)
#     # BTCData[dic["timestamp"]] = dic
#     BTCData.append(dic)

# # 去跟幣安抓資料
# kLines = BINANCE_CLIENT.get_historical_klines(
#     symbol, Client.KLINE_INTERVAL_1MINUTE, str(startTimestamp), str(endTimestamp))
# for k in kLines:
#     kLine = {
#         "timestamp": str(int(k[0] / 1000)),
#         "date": str(datetime.fromtimestamp(int(k[0] / 1000))),
#         "open": float(k[1]),
#         "high": float(k[2]),
#         "low": float(k[3]),
#         "close": float(k[4]),
#         "volume": float(k[5]),
#         "closeTimestamp": str(int((k[6] + 1) / 1000)),
#         "amount": float(k[7])
#     }
# # 整理成我們要用的
# if row["symbol"] == "ETHUSDT":
#     high = float(ETHQueryData[str(simuTime)]["high"])
#     low = float(ETHQueryData[str(simuTime)]["low"])
#     close = float(ETHQueryData[str(simuTime)]["close"])

# ======================================
# HW
# ======================================
# 註冊帳號，並完成此題
# https://leetcode.com/problems/two-sum/
