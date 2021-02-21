class person:
    # 定义基本属性
    name=""
    age=0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __hobby=""
    # 定义构造方法
    def __init__(self,n,a,h):
        self.name=n
        self.age=a
        self.__hobby=h
    def speak(self):
        print("%s 说：我 %d 岁。"%(self.name,self.age))


# 实例化类
p=person("sunny",18,"books")
p.speak() #sunny 说：我 18 岁。
