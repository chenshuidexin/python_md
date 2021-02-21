# 函数和模块的使用

# 定义函数 def关键字来定义函数，函数执行完成后通过 return 关键字来返回一个数值
# 所谓重构就是在不影响代码执行结果的前提下对代码的结构进行调整。

# def fac(num):
#     result = 1
#     for n in range(1, m+1):
#         result *= n
#     return result


# m = int(input("m= "))
# n = int(input("n= "))
# 当需要计算阶乘的时候不用在写循环求阶乘而是直接调用已经定义好的函数
# print(fac(m),"0220")
# print(fac(m) // fac(n) // fac(m-n))
# 在python的math模块中有一个名为 factorial 函数实现了阶乘运算


# 函数的参数 在python中函数的参数可以有默认值也支持可变参数，所以并不需要像其他语言一样支持函数的重载
# from random import randint


# def roll_dice(n=2):
#     # 摇色子
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total


# def add(a=0, b=0, c=0):  # 函数变量名不允许重复
# 三数相加
# return a+b+c


# 如果没有指定参数那么使用默认值摇两个色子
# print(roll_dice())
# 摇三颗色子
# print(roll_dice(3))


# 当我们不确定参数个数的时候，可以使用可变参数
# 在参数面前的* 表示args是一个可变参数
# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total


# 传入参数可以没有 也可以多个
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))


# 模块管理函数 由于python没有函数重载的概念，后面的定义会覆盖之前的定义，也就意味着同名函数实际上只有一个是存在的

def foo():
    print("hello,1111")


def foo():
    print("hello,2222")

foo()

# 如何解决命名冲突问题呢?
# python中每个文件代表了一个模块，在不同的模块中可以有同名的函数,在使用函数的时候通过import关键字导入指定的模块就可以区分到底使用哪个模块的foo函数

# 全局作用域  使用global关键字来指示变量来自于全局作用域
# 嵌套作用域  使用nonlocal关键字来指示变量来自于嵌套作用域

