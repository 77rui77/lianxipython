'''
对象的创建又称为类的实例化
语法：
    实例名=类名（）
'''

#创建类的语法
class Student:   #Student为类的名称（类名），由一个或多个单词组成，每个单词的首字母大写，其余小写
    pass

#python中一切皆对象。Student是对象吗？有内存空间吗
print(id(Student))
print(type(Student))
print(Student)

'''
类的组成：
        类属性
        实例方法
        静态方法
        类方法
'''

class Student:
    native_pace='吉林'  #直接写在类里的变量，称为类属性
    def __init__(self,name,age):
        self.name=name   #self.name称为实例属性，进行了一个赋值操作，将局部变量的name的值赋值给实例属性
        self.age=age

    #实例方法（在类之外定义的称为函数，在类之内定义的称为方法）
    def eat(self):
        print('学生在吃饭，，，')

    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

#创建Student类的对象
stu1=Student('张三',20)
stu1.eat()    #对象名.方法名()
print(stu1.name)
print(stu1.age)

print('-------------------------')
Student.eat(stu1)  #51行与46行代码功能相同，都是调用Student类中的eat方法
                    #类名.方法名(类的对象)-->实际上就是方法定义处的self
'''
print(id(stu1))
print(type(stu1))
print(stu1)
print('-------------------------')
print(id(Student))#Student是类的名称
print(type(Student))
print(Student)
'''
