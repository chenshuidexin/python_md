# 练习一:在屏幕上显示跑马灯文字

# import os
# import time

# def  main():
#     content="北京欢迎你，为你开天辟地..."
#     while True:
#         # 清空屏幕上的输出
#         os.system("cls") # os.system('clear')
#         print(content)
#         # 休眠200ms
#         time.sleep(0.2)
#         content=content[1:]+content[0]

# if __name__ == "__main__":
#     main()


# 练习二:设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成

# import random


# def generate_code(code_len=4):
#     '''
#     生成指定长度的验证码
#     :param code_len:验证码的长度(默认4个字符)

#     :return 由大小写英文字母和数字构成的随机验证码
#     '''
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars)-1  # 总共个数
#     code = ""
#     for _ in range(code_len):  # 循环code_len次数
#         index = random.randint(0, last_pos)  # 随机数字
#         code += all_chars[index]  # 循环到的数字对应的val相加
#     return code


# print(generate_code())


# 练习三:设计一个函数返回给定文件名的后缀名

# def get_suffix(filename, has_dot=False):
#     """
#     获取文件名的后缀名
#     :param  filename: 文件名m
#     :param  has_dot:返回的后缀名是否需要带点
#     :return :文件的后缀名
#     """
#     pos = filename.rfind(".") # 返回字符串最后一次出现的位置
#     if 0 < pos < len(filename)-1:
#         index = pos if has_dot else pos+1 # 设置为true的时候增加一个数字
#         return filename[index:]  # 返回的是后缀名
#     else:
#         return ""


# print(get_suffix('seey.txt', True)) # .txt


# 练习四:设计一个函数返回传入的列表中最大和第二大元素的值

# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2


# print(max2([11, 22, 22, 23, 33, 25]))  # (33, 25)


# 练习五:计算指定的年月日是这一年的第几天
# def is_leap_year(year):
#     '''
#     判断指定的年份是不是闰年

#     :param year:年份
#     :return :闰年返回True平年返回False
#     '''
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# def which_day(year, month, date):
#     '''
#     计算传入的日期是这一年的第几天

#     :param year:年
#     :param month:月
#     :param date:日
#     :return :第几天
#     '''
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)]
#     total = 0
#     for index in range(month-1):
#         total += days_of_month[index]
#     return total + date


# def main():
#     print(which_day(1980, 11, 28)) # 333
#     print(which_day(1981, 12, 31)) # 365
#     print(which_day(2018, 1, 1))   # 1
#     print(which_day(2021, 2, 26))  # 57


# if __name__ == "__main__":
#     main()


# 练习六:打印杨辉三角

def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
