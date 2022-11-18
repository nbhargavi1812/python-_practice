# x=list(range(1,11))
# print(x)
# x=[10,20,30,40]
# from functools import reduce
# z=reduce(lambda a,b:b-a,x)
# print('sub',z)
# o/p:-
# sub 20
# #
# class A:
#     def colour(self):
#         print('python')
#         print('alphabets')
#     def human(self ):
#         print('girls')
#     class B:
#         def subjects(self):
#             print('maths')
#         def groups(self):
#             print('mpc')
# obj=A()
# obj.B().groups()
# obj.human()
# obj.B().subjects()
# O/P:-
# mpc
# girls
# maths

#
#.

# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def student(self):
#         print('name:',self.name)
#         print('age:',self.age)
# obj=A('PYTHON',45)
# obj.student()
# print(obj.__dict__)
# o/p:-
# name: PYTHON
# age: 45
# {'name': 'PYTHON', 'age': 45}


#
# class B:
#     def __init__(self,a):
#         self.x=a
#     def python(self):
#
#          print('the data:',self.x)
# class T:
#     def modify(self,obj):
#         objB.x=objB.x+500
#         print('modify data:',objB)
# objB=B(200)
# objB.python()
# obj2=T()
# T().modify(objB)
# o/p:-
# the data: 200
# modify data: <__main__.B object at 0x000001921EEF7FD0>



#
#
# class x:
#     count=0
#     def __init__(self):
#         x.count=x.count+1
#     def python(self):
#         print('number of objects:',x.count)
# obj1=x()
# obj2=x()
# obj3=x()
# obj4=x()
# obj5=x()
# obj5.python()

#
# class A:
#     @staticmethod
#     def PYTHON():
#         A.x=1000
#         print('static method')
#         print('static method:', A.x)
# obj=A()
# A.PYTHON()
# O/P:-
# static method
# static method: 1000


