class Student():
    def __init__(self,name): # 初始化函数
        self.name=name

    def say_hi(self):
        print("hello,I'm {}".format(self.name))

kaibao=Student('kaibao');
kaibao.say_hi()

kkw=Student("kkw");
kkw.say_hi()