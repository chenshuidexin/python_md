# 字符串  由零个或多个字符组成的有限序列，在python程序中，如果我们把单个或多个字符用单引号或双引号包围起来就可以表示一个字符串

# 以三个双引号或者单引号开头的字符串可以折行

# 可以在字符串中使用 \ 反斜杠  \n表示换行  \t表示制表符

# s1 = '\'hello,kkw!\''
# s2 = 'nihao \n\hello,sunny!\\\n sunny'
# print(s1, s2, end='')


# 在\后面可以跟一个八进制或者十六进制来表示字符，例如\141和\x61都代表着小写字母a，前者是八进制的表示法，后者是十六进制的表示法。也可以在\后面跟Unicode字符编码来表示字符

# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\n\u9a86'
# print(s1, s2)

# 如果不希望字符串中\表示转义,可以通过在字符串的最前面加上字母r来加以说明

# s1=r"\'hello,s1!\'"
# s2=r"\n\\hello,world!\\\n"
# print(s1,s2,end="kw")


'''
python为字符串类型提供了非常丰富的运算符，可以使用+运算符实现字符串的拼接，可以使用*运算符来重复一个字符串的内容，可以使用in和not in 来判断一个字符串是否包含另外一个字符串(成员运算)，我们也可以使用[]和[:]运算符从字符串取出某个字符或某些字符(切片字符)
'''
# s1 = "sunny "*3
# print(s1)  # sunny sunny sunny
# s2 = "world"
# s1 += s2
# print(s1)  # sunny sunny sunny world
# print('nn' in s1)  # True
# print("good" in s1)  # False


# str2 = "abcde123456"
# # 从字符串中取出指定位置的字符(下标运算)
# print(str2[2]) #c
# # 字符串切片[从指定的开始索引到指定的结束索引)
# print(str2[2:5]) # cde
# print(str2[2:]) # cde123456
# print(str2[2::2]) # ce246
# print(str2[::2]) # ace246
# print(str2[::-1]) # 字符串翻转 654321edcba
# print(str2[-3:-1]) # 45  最后一个字符串不包含进去

# *******在python中可以使用这些方法处理字符串*******
# str1="hello, world!"
# 通过内置函数len计算字符串的长度
# print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
# print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
# print(str1.title()) # Hello, World!
# 获得字符串变大写的拷贝
# print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找字符串所在的位置
# print(str1.find("or")) # 8 查找之后返回的是字符串下标位置
# print(str1.find("shit")) # -1 查找不到就返回-1
# 与find类似但找不到子字符串的时候会引发异常
# print(str1.index("or")) # 8
# print(str1.index("shit"))  # 报异常
# 检查字符串是否以指定的字符串开头 区分大小写
# print(str1.startswith("He")) # False
# print(str1.startswith("hel")) # True
# 检查字符串是否以指定的字符串结尾
# print(str1.endswith("!")) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
# print(str1.center(50,"*")) # ******************hello, world!*******************
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
# print(str1.rjust(50,"_")) # _____________________________________hello, world!


# str2 = "abc123456"
# 检查字符串是否由数字构成
# print("数字", str2.isdigit())  # False
# 检查字符串是否由字母构成
# print("字母", str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
# print("数字和字母", str2.isalnum())  # True

# str3 = '      1140225945@qq.com'
# print(str3)  # 1140225945@qq.com
# 获得字符串修剪左右两侧空客之后的拷贝  清空字符串前后的空格
# print(str3.strip())  # 1140225945@qq.com


# 可以格式化输出字符串
# a, b = 5, 9  # 输出格式：5*9=45
# print("%d*%d=%d" % (a, b, a*b))
# 可以使用字符串提供的方法来完成字符串的格式
# print('{0}*{1}={2}'.format(a, b, a*b))
# python3.6之后，格式化字符串还有更简洁的书写方式
# print(f'{a}*{b}={a*b}')


# 数值类型(int和float)是标量类型，这种类型的对象没有可以访问的内部结构
# 列表
# 列表和字符串是一种结构化，非标量类型，因此才会有一系列的属性和方法
# list1 = [1, 3, 5, 7, 9, 11]
# print(list1) # [1, 3, 5, 7, 9, 11]
# * 乘号表示列表元素的重复
# list2 = ["sunny","rain"]*4 # ['sunny', 'rain', 'sunny', 'rain', 'sunny', 'rain', 'sunny', 'rain']
# print(list2) # ['sunny', 'rain', 'sunny', 'rain', 'sunny', 'rain', 'sunny', 'rain']
# 计算列表长度(元素个数)
# print(len(list1)) # 6
# 下标(索引)运算
# print(list1[0]) # 1
# print(list1[3]) # 7
# print(list1[7]) # IndexError: list index out of range
# print(list1[-1]) # 11
# print(list1[-3]) # 7
# list1[2] = 22
# print(list1) # [1, 3, 22, 7, 9, 11]
# 通过循环用下标遍历列表元素
# for index in range(len(list1)):
# print("index",list1[index])

# 通过for循环遍历列表
# for elem in list1:
# print("elem",elem)

# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
# for index, elem in enumerate(list1):
# print(index, elem)


# 列表中对元素的增删改查
list3 = [1, 3, 5, 7, 9]

# 添加元素
list3.append(200)  # 最后末尾增加数值200
# print(list3) # [1, 3, 5, 7, 9, 200]
list3.insert(1, 400)  # 索引值为1的地方前面插入数值400
# print(list3) #[1, 400, 3, 5, 7, 9, 200]

# 合并两个列表
# list3.extend([111,222])
# print(list3) # [1, 400, 3, 5, 7, 9, 200, 111, 222]
list3 += [333, 444]  # 合并表格的另一种表示方式
# print(list3) # [1, 400, 3, 5, 7, 9, 200, 333, 444]
# print(len(list3)) # 9

# 先通过成员运算判断元素是否在列表中，如果存在就删除
if 5 in list3:
    list3.remove(5)
if 123 in list3:  # 不存在的数值也不会报错
    list3.remove(123)
# print(list3) # [1, 400, 3, 7, 9, 200, 333, 444]

# 从指定的位置删除元素
list3.pop(0)  # 删除下标为0的数值
# print(list3) # [400, 3, 7, 9, 200, 333, 444]
list3.pop(len(list3)-1)  # 删除列表中最后一位数字
# print(list3) # [400, 3, 7, 9, 200, 333]

# 清空列表
list3.clear()
# print(list3) # []

# 和字符串一样，列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建新的列表
fruits = ["grape", "apple", "strawberry", "waxberry"]
fruits += ["pitaya", "pear", "mango"]
# print(fruits) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']


# 列表切片
fruits2 = fruits[1:4]
# print(fruits2) # ['apple', 'strawberry', 'waxberry']

# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]  # 完整复制一份列表
# print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]  # [-3,-1)
# print(fruits4) # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]  # 获得是翻转后的列表
# print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']

# 实现对列表的排序操作
listt1 = ["orange", "apple", "zoo", "internationalization", "blueberry"]
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
listt2 = sorted(listt1)
# print(listt2) # ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']
listt3 = sorted(listt1, reverse=True)
# print(listt3) # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
listt4 = sorted(listt1, key=len)  # 从短到长进行排序
# print(listt4) # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']
# 给对象列表发出排序消息直接在列表对象上进行排序
listt1.sort(reverse=True)
# print(listt1) # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']

# 生成式和生成器
# 使用列表的生成式语法来创建列表
f = [x for x in range(1, 10)]
# print(f)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = [x+y for x in "ABCDE" for y in "1234567"]
# print(f)  # ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']

# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以消耗较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
# 查看对象所占用内存的字节数
# print(sys.getsizeof(f))
# print(f)

# 需要注意的是:下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器对象可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
# f = (x**2 for x in range(1, 1000))
# print(sys.getsizeof(f)) # 相比生成式生成器不占用存储数据的空间
# print(f)
# for val in f:
# print(val)

# 除了上面的生成器语法，py中还有另外一种定义生成器的方式，就是通过`yield`关键字将一个普通函数改造成生成器函数。
# 斐波拉切数列


# def fib(args):
#     a, b = 0, 1
#     for _ in range(10):
#         a, b = b, a+b
#         yield a


# def main():
#     for val in fib(20):
#         print(val)


# if __name__ == "__main__":
#     main()


# 元组的使用
# python中的元组和列表类似也是一种容器数据类型，可以用一个变量(对象)来存储多个数据，不同之处在于元组的元素不能修改。

# 定义元组
t = ("sunny", 22, "beijing", False)
# print(t) # ('sunny', 22, 'beijing', False)

# 获取元组中的元素
# print(t[0]) # sunny
# print(t[3]) # False
# 遍历元组中的值
# for member in t:
# print(member)

# 重新给元组赋值
# t[0]="rain" # TypeError: 'tuple' object does not support item assignment
# 变量t重新引用了新的元组  原来的元组将被垃圾回收
t = ('rain', 22, False, "hebei")
# print(t) # ('rain', 22, False, 'hebei')

# 将元组转换成列表
person = list(t)
# print(person) # ['rain', 22, False, 'hebei']
# 列表是可以修改元素的
person[0] = "kkw"
person[1] = 8
# print(person) # ['kkw', 8, False, 'hebei']

# 将列表转换成元组
fruits_list = ["orange", "banan", "apple"]
fruits_tuple = tuple(fruits_list)
# print(fruits_tuple) # ('orange', 'banan', 'apple')

'''
这里有一个值得探讨的问题，我们明明已经有了列表数据结构，为什么还需要元组这样类型的呢?

1.元组中的元素是无法修改的，事实上我们在项目中尤其是多线程环境中可能更喜欢使用的是那些不变的对象(一方面因为对象状态不能修改，所以可以避免由此引起的不必要的程序错误，简单的说就是一个不变的对象要比可变的对象更容易维护;另一方面因为没有任何一个线程能够修改不变对象的内部状态，一个不变对象自动就是线程安全的，这样就可以省掉处理同步化的开销。一个不变对象可以方便的被共享访问)。所以结论是:如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组，当然如果一个方法要返回多个值，使用元组也是不错的选择

2.元组在创建时间和占用的空间上都优于列表。我们可以使用sys模块的getsizeof函数来检查存储同样的元素的元组和列表各自占用了多少内存空间。这个很容易做到的。我们可以在ipython中使用魔法指令 %timeit来分析创建同样内容的元组和列表所花费的时间。
'''

# py中的集合
# 跟数学上的集合是一致的,不允许有重复元素，而且可以进行交集、并集、差集等等运算

# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 4}
# print(set1)  # {1, 2, 3, 4}
# print("Leng = ", len(set1)) # Leng =  4
# 创建集合的构造器语法(等到面向对象部分会详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 4, 3, 2, 1))
# print(set2,set3) # {1, 2, 3, 4, 5, 6, 7, 8, 9} {1, 2, 3, 4}
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 13 == 0 or num % 15 == 0}
# print(set4) # {65, 90, 39, 75, 13, 45, 15, 78, 52, 26, 91, 60, 30}

# 向集合添加元素和删除元素
set1.add(4)
set1.add(5)
# print(set1) # {1, 2, 3, 4, 5}
set2.update([11, 12])
set2.discard(5)  # discard 丢弃,抛弃
# print(set2) # {1, 2, 3, 4, 6, 7, 8, 9, 11, 12}
if 4 in set2:
    set2.remove(4)
# print("set1",set1) # set1 {1, 2, 3, 4, 5}
# print("set2",set2) # set2 {1, 2, 3, 6, 7, 8, 9, 11, 12}
# print(set3.pop()) # 1  返回值是删除的数值
# print("set3",set3) # set3 {2, 3, 4}

'''
说明:Python中允许通过一些特殊方法来为某种类型或数据结构自定义运算符(后面的章节会讲解到),下面的代码中我们对集合进行运算的时候可以调用集合对象的方法，也可以直接使用对应的运算符，例如&运算符和intersection方法的作用是一样的，但是使用运算符让代码更加直观。
'''
# 集合的交集、并集、差集、对称差运算
# print(set1,set2) # {1, 2, 3, 4, 5} {1, 2, 3, 6, 7, 8, 9, 11, 12}
# 交集  {1, 2, 3}
# print(set1 & set2)
# print(set1.intersection(set2))
# 并集  {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
# print(set1 | set2)
# print(set1.union(set2))
# 差集 {4, 5} set1 减去共同有的部分
# print(set1-set2)
# print(set1.difference(set2))
# 差集的合体 set1+set2合体减去交集的部分  {4, 5, 6, 7, 8, 9, 11, 12}
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))

# print(set1, set2, set3) # {1, 2, 3, 4, 5} {1, 2, 3, 6, 7, 8, 9, 11, 12} {1, 2, 3, 4} set1和set3有关系
# 判断子集和超集   False
# print(set2 <= set1)
# print(set2.issubset(set1))
# True
# print(set3 <= set1)
# print(set3.issubset(set1))
# False
# print(set1 >= set2)
# print(set1.issuperset(set2))
# True
# print(set1 >= set3)
# print(set1.issuperset(set3))


# 字典的使用
# 字典是另一种可变容器模型，它可以存储任意类型对象，与列表、集合不同的是:字典的每个元素都是由一个键和一个值组成的"键值对",键和值通过冒号分开。

# 创建字典的字面量语法
scores = {"name": "sunny", "age": 12, "address": "beijing"}
# print(scores)  # {'name': 'sunny', 'age': 12, 'address': 'beijing'}
# 创建字典的构造器语法
item1 = dict(one=1, two=2, three=3, four=4)
# print(item1) # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# 通过zip函数将两个序列压成字典
item2 = dict(zip(["a", "b", "c"], "123"))
# print(item2) # {'a': '1', 'b': '2', 'c': '3'}
# 创建字典的推导式语法
item3 = {num: num**2 for num in range(1, 10)}
# print(item3) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# 通过键值对可以获取字典中对应的值
# print(scores['name']) # sunny
# print(scores['address']) # beijing

# 对字典中所有键值对进行遍历
# for key in scores:
# print(f'{key}:{scores[key]}') #name:sunny      age:12      address:beijing

# 更新字典中的元素
scores["name"] = "kkw"
scores["hobby"] = "swimming"
scores.update(eat=55, drink=66)
# print(scores) # {'name': 'kkw', 'age': 12, 'address': 'beijing', 'hobby': 'swimming', 'eat': 55, 'drink': 66}
if "name" in scores:
    print(scores["name"])  # kkw
print(scores.get("age"))  # 12 get方法是通过键获取对应的值但是可以设置默认值
print(scores.get("sunny", 1))  # 返回的是默认值

# 删除字典中的元素
print(scores.popitem()) # 删除的是最后一个键值对 ('drink', 66)
print(scores.popitem()) # 删除的是最后一个键值对 ('eat', 55)
print(scores.pop("name", "kkw")) # kkw 直接删除特定的值

# 清空字典
scores.clear()
print(scores) # {}
