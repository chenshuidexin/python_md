# 练习1：定义一个类描述数字时钟
'''
from time import sleep


class Clock(object):
    # 数字时钟
    def __init__(self, hour=0, minute=0, second=0):
        # 初始化方法
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        # 显示时间
        return '%02d:%02d:%02d' %\
            (self._hour, self._minute, self._second)


def main():
    clock = Clock(14, 59, 22)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == "__main__":
    main()
'''

# 练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法

from math import sqrt


class Point(object):
    def __init__(self, x=0, y=0):
        # 初始化方法
        self.x = x
        self.y = y

    def move_to(self, x, y):
        # 移动位置
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        # 横纵坐标的增量
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        # 计算与另外一个点的距离
        dx = self.x-other.x
        dy = self.y-other.y
        return sqrt(dx**2+dy**2)

    def __str__(self):
        return '(%s,%s)'%(str(self.x),str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == "__main__":
    main()
