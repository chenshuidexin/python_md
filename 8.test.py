'''
面向对象编程
把一组数据结构和处理方法组成对象，把相同行为的对象归纳为类，通过类的封装隐藏内部细节，通过继承实现类的特化和泛化，通过多态实现基于对象类型的动态分派

"程序是指令的集合"，在程序书写的语句在执行时会变成一条或多条指令然后由cpu去执行。引入函数的概念，把相对独立且经常重复使用的代码放置函数中，在需要使用这些功能的时候只需要调用函数即可；如果一个函数的功能过于复杂和臃肿，可以进一步将函数继续切分为子函数来降低系统的复杂性

按照面向对象的编程理念，程序中的数据和操作数据的函数是一个逻辑上的整体，称之为"对象"，而解决问题的方式是创建出需要的对象并向对象发出各种各样的消息，多个对象的协同工作最终可以构造出复杂的系统来解决现实中的问题

'''

# 类和对象

# 简单来说，类是对象的蓝图和模板，对象是类的实例。 类是概念，对象是具体的东西
# 在面向对象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定是属于某个类(型)。当我们把这些共同特征的对象的静态特征(属性)和动态特征(行为)都抽取后，就可以定义一个叫做"类"的东西

# 定义类  在py中使用 class 关键字定义类，然后在类中通过函数定义方法，可以将对象的动态特征描述出来


class Student(object):
    # __init__是一个特殊的方法用于创建对象时进行初始化操作
    # 通过这个方法可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # 要求标识符的名字全小写多个单词用下划线链接，当然有的工作是用驼峰命名法
    def watch_movie(self):
        if self.age < 18:
            print('%s只能看蓝猫' % self.name)
        else:
            print("%s可以看道德思想政治" % self.name)

# 写在类中的函数，称之为(对象的)方法，这些方法是对象可以接收的消息


# stu = Student("kkw", 8)
# stu.study("English")
# stu.watch_movie()


# 创建和使用对象
# 当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息

def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student("kkw", 23)
    # 给对象发study消息
    stu1.study("程序设计")
    # 给对象发送watch_movie消息
    stu1.watch_movie()
    stu2 = Student("sunny", 11)
    stu2.study("前端开发")
    stu2.watch_movie()


if __name__ == "__main__":
    main()


'''
访问可见性问题
给 Student 对象绑定的name和age属性有怎样的访问权限?在很多面向对象编程语言中，会将对象的属性设置为私有的(private)和受保护的(protected)，简单来说就是不允许外界访问，而对象的方法通常是公开的(public)，因为公开的方法就是对象能够接收的消息。在python中，属性和方法的权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在属性命名时可以用两个下划线作为开头
'''

'''
class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar")


def main():
    test = Test("hello")
    #  AttributeError: 'Test' object has no attribute '__bar'
    # test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    # print(test.__foo)


if __name__ == "__main__":
    main()
'''

# 但是，python并没有从语法上严格保证私有属性或方法的私密性，只是给私有属性和方法换了一个名字来妨碍对它们的访问，事实上如果知道了更换名字的规则仍然可以访问到它们。。之所以这样设定，可以用这样一句名言加以解释，就是"We are all consenting adults here"。因为绝大多数程序员都认为开放比封闭要好，而且程序员要自己为自己的行为负责。


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # #################
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()


'''
在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重。这种做法并不是语法上的规则，单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻
'''