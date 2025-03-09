# # # # lst=['京A88888','沪A66666','陕A00001']
# # # # for item in lst:
# # # #     area=item[0:1]
# # # #     print(item,area)
# # # # s='HelloPython,HelloJava'
# # # # word=input('请申诉')
# # # # print('{0}zai{1}zhongchuxianle{2}ci'.format(word,s,s.upper().count(word)))
# # # # list1=[
# # # #     ['01','phone','Apple','13999'],
# # # #     ['02','microwave','XiaoMi','1399'],
# # # #     ['03','TV','TCL','39999'],
# # # # ]
# # # # print('编号\t\t名称\t\t品牌\t\t价格')
# # # # for item in list1:
# # # #     for i in item:
# # # #         print(i,end='\t\t')
# # # #     print()
# # # # for item in list1:
# # # #     item[0]='0000'+item[0]
# # # #     item[3]='${0:.2f}'.format(float(item[3]))
# # # # for item in list1:
# # # #     for i in item:
# #         print(i,end='\t\t')
# #     print()
# # try:
# #     num1=int(input())
# # except ZeroDivisionError:
# #     print('除数为零')
# # else:
# #     pass
#
# # finally:
# #     pass
# # def cal2(a,b):
# #     s=a+b
# #     return s
# # get=cal2(1,2)
# # print(get)
# #
# # lst=[10,20,30,40]
# # for i in range(len(lst)):
# #     print(lst[i])
# # print()
# # for i in range(len(lst)):
# #     result=lambda x:x[i]
# #     print(result(lst))
# # student_scores={
# #     {'name':'jack','score':'30'}
# # }
# # def fibonacci(n):
# #     if n==1 or n==2:
# #         return 1
# #     else:
# #         return fibonacci(n-1)+fibonacci(n-2)
# #
# # print(fibonacci(9))
#
#
# # a,b=0,1
# # for i in range(1,9):
# #     a,b=b,a+b
# #
# #
# #     print(a)
# import random
#
#
# # print(bool(0.5))
# # print(divmod(12,5))
# # print(max('hello'))
# # print(sum([1,2,3]))
# # def Max(lst):
# #     x=lst[0]
# #     for i in range(1,len(lst)):
# #         if lst[i]>x:
# #             x=lst[i]
# #     return x
# # lst=[random.randint(1,100) for item in range(10)]
# # print(lst)
# # max=Max(lst)
# # print(max)
#
# # s=input('请输入一个字符串：')
# # def get_digit(s):
# #     sd=0
# #     lst=[]
# #     for item in s:
# #         if item.isdigit():
# #             lst.append(int(item))
# #     sd=sum(lst)
# #     return lst,sd
# # lst,x=get_digit(s)
# # print(lst,x)
#
# # def lower_upper(x):
# #     lst=[]
# #     for item in x:
# #         if 'A'<=item<='Z':
# #             lst.append(chr(ord(item)+32))
# #         elif 'a'<=item<='z':
# #             lst.append(chr(ord(item)-32))
# #         else:
# #             lst.append(item)
# #     return ''.join(lst)
# # s=input('请输入一个字符串：')
# # o=lower_upper(s)
# # print((o))
#
# #
# # def getfind(s,lst):
# #     for item in lst:
# #         if s==item:
# #             return True
# #     return False
# # lst=['hello']
# # s=input('please input your sentence')
# # result=getfind(s,lst)
# # print('exist'if result else'not exist')
#
# # class Student():
# #     def __init__(self,xm,age,weight):
# #         self.name=xm
# #         self.age=age
# #         self.__weight=weight
# #     def show(self):
# #         print(f'My name is {self.name},I\'m {self.age} years old',{self.__weight})
# #     @property
# #     def weight(self):
# #         return self.__weight
# #     @weight.setter
# #     def weight(self,value):
# #         pass
# #
# # stu1=Student('linda',21,30)
# # stu1.show()
#
#
# # a=10
# # b=20
# # print(a.__add__(b))#+
# # print(a.__sub__(b))#-
# # print(a.__lt__(b))#<
# # print(a.__eq__(b))#=
# # print(a.__le__(b))#<=
# # print(a.__ge__(b))#>=
# # print(a.__gt__(b))#>
# # print(a.__mul__(b))#*
# # print(a.__truediv__(b))#/
# # print(a.__mod__(b))#%
# # print(a.__floordiv__(b))#//
# # print(a.__pow__(b))#幂运算
#
# # class F:
# #     pass
# # class U:
# #     pass
# # class C(F, U):
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# # a = F()
# # u = U()
# # c = C('jerk', 22)
# # print(a.__dict__, a.__class__, F.__bases__, F.__base__, C.__mro__)
# # class Circle:
# #     def __init__(self,r):
# #         self.r=r
# #     def getarea(self):
# #         return 3.14*self.r*self.r
# #     def getperimeter(self):
# #         return 2*3.14*self.r
# #
# # r=eval(input('请输入圆的半径'))
# # c=Circle(r)
# # area=c.getarea()
# # perimeter=c.getperimeter()
# # print('圆的面积为：',area,'圆的周长为：',perimeter)
#
# # class Student:
# #     def __init__(self,name,age,gender,score):
# #         self.name=name
# #         self.age=age
# #         self.gender=gender
# #         self.score=score
# #     def info(self):
# #         print(self.name,self.age,self.gender,self.score)
# #
# # print('请输入五位学生的信息：（姓名#年龄#性别#分数）')
# # lst=[]
# # for i in range(1,6):
# #     s=input(f'请输入第{i}位学生信息')
# #     s_lst=s.split('#')
# #     stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])
# #     lst.append(stu)
# # for item in lst:
# #     item.info()
#
# class Instrument:
#     def make_sound(self):
#         pass
# lass Erhu(Instrument):
# def make_sound(self):
#     print('二胡在演奏')
# class Piano(Instrument):
#     def make_sound(self):
#         print('钢琴在演奏')
# class Violin(Instrument):
#     def make_sound(self):
#         print('小提琴在演奏')
# def play(obj):
#     obj.make_sound()
# erhu=Erhu()
# piano=Piano()
# violin=Violin()
# play(erhu)
# play(piano)
# play(violin)
class Vehicle:
    def __init__(self,model,code):
        self.model=model
        self.code=code
    def setup(self):
        print('车辆已启动')
    def setdown(self):
        print('车辆已停止')
class Cab(Vehicle):
    def cab1(self):
        print('出租车来了！！！')
    def __init__(self,mode,code,company):
        super().setup()
        super().setdown()
        super().__init__(mode,code)
        self.company=company

class FamilyCar(Vehicle):
    def f1(self):
        print('你爹来了！！！')
    def __init__(self, mode, code, name):
        super().setup()
        super().setdown()
        super().__init__(mode, code)
        self.name = name

taxi=Cab('奔驰','京A00001','中华人民共和国国务院')
taxi.cab1()

familycar=FamilyCar('劳斯莱斯','京A12345','你爹')
familycar.f1()
