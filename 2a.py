# 2a
# insert
# 題目敘述:有一升冪數列，今有一數字需放入其中，並且結束後仍須為升冪數列
x = int(input("插入一數字 : "))
List1 = [1, 5, 8, 12, 20, 200]

# counter=0
# for ele in List1:
#     if ele < x:
#         counter+=1

# print(counter) #我想要取代的位置，我想要放進去的位置

# List1.insert(counter,x)

# print(List1)
for i in range(len(List1)):
    if x < List1[i]:
        List1.insert(i, x)
        break
    elif i == len(List1) - 1:
        List1.append(x)

print(List1)


# print("原數列", List1)
# print("插入", x)
