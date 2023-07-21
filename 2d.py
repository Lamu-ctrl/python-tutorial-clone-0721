# 2d 質數判斷
# 找出 0~20 中的質數 放到一個list中

# 判定 任意數 是否為質數
list=[]
for x in range(0,21):

    if x == 0 or x==1:
        print("例外")
    else:
        flag=True
        for i in range(2,x):
            # print( i )
            if x % i ==0:
                print( i )
                flag=False

        if flag == True:
            print("prime")
            list.append(x)
        else :
            print("nono")

print(list)