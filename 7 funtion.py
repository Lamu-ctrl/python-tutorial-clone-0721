
# # ======================================
# # # function
# # ======================================
# def sum(a, b):

#     print(a)
#     print(b)
#     print(a+b)
#     print("end")  # 去掉一個解釋執行順序


# sum(5, 10)

# # ======================================
# # return


# def sum(a, b):
#     return a+b


# x = sum(5, 10)
# print(sum(5, 10))
# print(type(x))


# def sum(a, b):

#     print(a)
#     print(b)
#     print(a+b)
#     print("end")  # 去掉一個解釋執行順序


# x = sum(5, 10)
# print(x)


# # ======================================
# # 關鍵字參數(Keyword Argument)

# def sum(a, b):
#     return a+b


# x = sum(a=5, b=10)
# print(sum(5, 10))
# print(type(x))

# ======================================
# 預設值參數(Default Argument)：在函式定義的參數中，將可以選擇性傳入的參數設定一個預設值，
# 當來源端有傳入該資料時，使用來源端的資料，沒有傳入時，則依照設定的預設值來進行運算，如下範例：


# def sum(a, b, c=10):
#     return a+b+c


# x = sum(a=5, b=10)
# print(sum(5, 10))
# print(type(x))

# def sum(a, b, c=None):
#     if c == None:
#         return a+b
#     else:
#         return a+b+c


# print(sum(5, 10))
# print(sum(5, 10, 10))


# ======================================
# 函式(Function) *args、**kwargs運算子

# def app_log(*info):
#     print(info)


# app_log("mike", "a", "202")  # 從執行結果可以看到，Python會將參數資料打包成元組(Tuple)資料型態，
# # https://selflearningsuccess.com/python-tuple/

# # 傳 list
# list = ["mike", "a", "202"]
# app_log(list)

# # 說明
# # 定義過多參數會使可讀性降低，並且如果你並不知道可能會傳入多少參數，想要使funtion具有彈性時
# # print("a","b","c")


# # **kwargs  想打包成字典(Dictionary)資料型態，則可以使用 ** 符號，


# def app_log(**info):
#     print(info)


# app_log(name="mike", dom="a", room="202")


# # ======================================
# # # 變數
# # ======================================

# 函式(Function)變數範圍(Scope)
# 一、 變數
# http://c.biancheng.net/view/2258.html

# def swap(a, b):
#     # 下面代码实现a、b变量的值交换
#     a, b = b, a
#     print("swap函数里，a的值是",
#           a, "；b的值是", b)


# a = 6
# b = 9
# swap(a, b)
# print("交换结束后，变量a的值是",
#       a, "；变量b的值是", b)

# 區域變數(Local Variable) 和全域變數(Global Variable)

# ======================================
# # 1. local

# # 說明1
# x = 20
# print("outside", id(x))


# def plus1(x):
#     x = x+1
#     print("inside", id(x))
#     print(x)


# print("outside", id(x))
# plus1(20)
# # print("outside",id(x))
# print(x)

# 範例2
# def funtion1():
#     x=100

# print(x)

# ======================================

# 2.global
# x = 20
# def funtion1():
#     x=100

# print(x)


# # ======================================
# # # 大總結
# # ======================================
# 為何要使用funtion


#  範例 : xlsx_preprocess_and_merge_to_csv
#
#  以 netflix crawler 為例
#
#  測試
#  爬取
#  儲存
