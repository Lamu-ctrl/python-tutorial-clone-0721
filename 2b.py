# 2b reverse
# 有一數列，請倒置這數列
# 說明  [ 1 , 5 , 8 ]  reverse後為 [8,5,1]
# 第一個變最後一個，最後一個變第一個
List1 = [1, 5, 8, 12, 20, 200]
# a. 請放到 List2 給我

List2 = []
for i in range(len(List1)-1, -1, -1):
    List2.append(List1[i])

print(List2)