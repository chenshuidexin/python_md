'''
sum=0
for x in range(100,0,-2):
    sum+=x

print(sum)
'''
'''
# 猜数字大小游戏
import random

answer=random.randint(1,100) # 从中选择一个整数
counter=0
while True:
    counter +=1
    number=int(input("请输入数字:"))
    if number < answer:
        print("大一些")
    elif number > answer:
        print("小一些")
    else:
        print("恭喜猜对啦!")
        break
print("你总共猜对了 %d 次" % counter)

if counter>7:
    print("智商明显不足呀 ^_^")
else:
    print("聪明人呀!")
'''
'''
# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d" % (i,j,i+j),end="\t")
    print("结束啦")
'''
'''
# 最大公约数和最小公倍数
# 两个数的最大公约数是两个数的公共因子中最大的那个数;两个数的最小公倍数则是能够同时被两个数整除的最小的那个数

x=int(input("x= "))
y=int(input("y= "))
# 如果x大于y就要交换x和y的值
if x>y:
    # 通过下面的方式xy值进行交换赋值
    x,y=y,x
# 从两个数中较大数字开始做递减的循环
for factor in range(x,0,-1):
    if x % factor == 0 and y % factor == 0:
        print("%d和%d的最大公约数:%d" % (x,y,factor))
        print("%d和%d的最小公倍数:%d" % (x,y,x*y//factor))
        break 
'''
# 小三角游戏

row=int(input("请输入行数: "))
for i in range(row):
    for _ in range(i+1):
        print("*",end=" ")
    print()

for i in range(row):
    for j in range(row):
        if j<row-i-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

for i in range(row):
    for _ in range(row-i-1):
        print(" ",end=" ")
    for _ in range(2*i+1):
        print("*",end=" ")
    print()