# 练习python语法，增加熟悉度

# 1.水仙花数：三位数，该数字每各位上数字的立方之和正好等于它本身。

# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100 # num除以100的结果向下取整
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

# num = int(input("num="))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num*10+num % 10  # 数字翻转
#     num //= 10 # n除以10的结果向下取整
# print(reversed_num)


# 2.百钱百鸡问题 穷举法也叫暴力搜索法

'''
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡
'''
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100-x-y
#         if 5*x+3*y+z/3 == 100:
#             print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (x, y, z))


# 3.craps赌博游戏：

from random import randint
money = 1000
while money > 0:
    print("你的总资产是：",money)
    needs_go_on = False
    while True: # 玩家的色子
        debt = int(input("请您下注:"))
        if 0 < debt <= money:
            break
    first = randint(1, 6)+randint(1, 6)  # 两个色子相加
    print("玩家玩出了%d点" % first)
    if first == 7 or first == 11:
        print("玩家胜利!")
        money += debt  # 加上下注的钱
    elif first == 2 or first == 3 or first == 12:
        print("庄家胜利!")
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:  # 庄家的色子
        needs_go_on = False
        current = randint(1, 6)+randint(1, 6)
        print("玩家摇出了%d点" % current)
        if current == 7:
            print("庄家胜")
            money -= debt
        elif current == first:
            print("玩家胜")
            money += debt
        else:
            needs_go_on=True
print("你破产了!")
