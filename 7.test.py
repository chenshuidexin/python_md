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


str2 = "abc123456"
# 检查字符串是否由数字构成
print("数字", str2.isdigit())  # False
# 检查字符串是否由字母构成
print("字母", str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print("数字和字母", str2.isalnum())  # True

str3 = '      1140225945@qq.com'
print(str3)  # 1140225945@qq.com
# 获得字符串修剪左右两侧空客之后的拷贝  清空字符串前后的空格
print(str3.strip())  # 1140225945@qq.com


# 可以格式化输出字符串
a, b = 5, 9  # 输出格式：5*9=45
print("%d*%d=%d" % (a, b, a*b))
# 可以使用字符串提供的方法来完成字符串的格式
print('{0}*{1}={2}'.format(a, b, a*b))
# python3.6之后，格式化字符串还有更简洁的书写方式
print(f'{a}*{b}={a*b}')
