# Q1. What is inheritance? how many types are there and example?
# A. Inheritance: Acquiring properties of one class data into another class data is called inheritance.
#     There are 5 types of inheritance.They are
# 1. Single inheritance:- inheriting the properties of one class into another class is called single inheritance.
#    Example:-
# class I:
#     def A1(self):
#         print('parent data')
# class J(I):
#     def A2(self):
#         print('child data')
# obj=J()
# obj.A2()
# obj.A1()
# o/p:-
# child data
# parent data
# 2. Multilevel inheritance:-inheriting the properties of multiple class into one class is called Multilevel inheritance.
# # Example:-
# class I:
#     def A1(self):
#         print('parent data')
# class J(I):
#     def A2(self):
#         print('child data')
# class K(J):
#     def A3(self):
#         print(' Sub child data')
# obj=K()
# obj.A3()
# obj.A2()
# obj.A1()
# O/P:-
#  Sub child data
# child data
#  parent data
# 3. Hierarchical inheritance:inheriting the properties of one class into  multiple class is called Hierarchical inheritance.
# Example:-
# class I():
#     def A1(self):
#         print('parent data')
# class J(I):
#     def A2(self):
#         print('chid 1 data')
# class K(J):
#     def A3(self):
#         print('child 2 data')
# obj=K()
# obj.A1()
# obj.A2()
# obj.A3()
# o/p:-
# parent data
# chid 1 data
# child 2 data
# 4. Multiple inheritance:inheriting the properties of multiple class into single class is called Multiple inheritance.
# Example:
# class I():
#     def A1(self):
#         print('class I data')
# class J():
#     def A2(self):
#         print('class J data')
# class K():
#     def A3(self):
#         print('class K data')
# class L(I,J,K):
#     pass
# obj=L()
# obj.A1()
# obj.A2()
# obj.A3()
# o/p:-
# class I data
# class J data
# class K data
# 5. Hybrid inheritance:- combination of more than one inheritance is called Hybrid inheritance.
# # Example:
# class I():
#      def A1(self):
#         print('class I data')
# class J():
#     def A2(self):
#         print('class J data')
# class K(I,J):
#     def A3(self):
#         print('class K  data')
# class L(K):
#     def A4(self):
#         print('class L data')
# obj=L()
# obj.A1()
# obj.A2()
# obj.A3()
# obj.A4()
# o/p:-
# class I data
# class J data
# class K  data
# class L data


# Q2. What is polymorpisam write an example?
# A.polymorpisam: An entity which represents in multiple forms is called polymorpisam.
#    Example: + operator  acts as concatenation and arithematic addition.
#              print(1+2)
#              print('A'+'B')

#
#
# Q3. Does function overloading is possible in python if no how manys ways you can achieve function overloading?
# A. Function overloading:
#    In python method overloading is not possible.
#    Most of the times ,if method with variables no.of arguments required then we can handle with default
#    arguments or variable length  arguments.


#
# Q4. What is operator overloading write an exanple?
# A. operator overloading: We can use the same operator for multiple purposes,which is known as operator overloading.
#      Python supports operator overloading.
#      Example:- '*' operator used for mutiplication and srting repetition.
#                 print(14*50)     #700
#                 print('good'*4)   #goodgoodgoodgood


#
# Q5. what is function overriding write an example?
# A. Function overriding:- The method which is present in parent class and derived class meethod with same
#    name and same arguments then parent class method is overridden b derived class method.
# Example:
# class B:
#     def chocolates(self):
#         print('munch')
#     def honey(self):
#         print('shivaansh')
# class C(B):
#     def honey(self):
#         print('pretheka')
#         super().honey()
# X=C()
# X.chocolates()
# X.honey()
# o/p:-
# munch
# pretheka
# shivaansh
#
#
# Q6.what is Abstract class write an example?
 # A. Abstract class: some times implimentation of class is not complete, such type of partially implimentation class are called Abstract class.
 #         But every abstract class in python should be derived from ABC class which is presented in abc module.
 # Example 1:
# from abc import *
 # class exam:
#     pass
 # t=exam()
 #         # we can create object for exam class as it doesn't contain any abstract method.

# Example 2:
# from abc import *
# class Test(ABC):
#     pass
# t=Test()
#          we can create object for Test class even it is in abstract class.
#  Example3 :
#  from abc import *
#  class Test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     t=Test()
#          we cannot create object for Test class as it contains abstract method.
# Example 4:
# from abc import *
# class Test():
#     @abstractmethod
#     def m1(self):
#         pass
#     t=test()
#         we can create object for Test class as it contains abstract method but not the ABC class.


#
# Q7. Create a class that accept 5 students data
class Z:
    def __int__(self,sname,rno):
        self.student=sname
        self.n=int(input('Enter no.of students:'))
        for i in self.student:
             if x==[]:
                rno=input('enter student no:')
                x.append(sname)
                sname=input('enter student name ')

obj=Z()




# Q8. What is Duck typing polymorphisam how to check particular method is exists or not in class?
# A. Duck typing: Different classes having same method with different functionality is called Duck typing polymorphisam.
#      example:
# class Duck:
#      def talk(self):
#           print('duck talk quack...quack')
# class Dog:
#      def talk(self):
#           print('dog talk bow..bow')
# class cat:
#      def talk(self):
#           print('cat talk meow...meow')
# x=[Duck(),Dog(),cat()]
# for i in x:
#      i.talk()
# o/p:-
# duck talk quack...quack
# dog talk bow..bow
# cat talk meow...meow



# Q9.Create a class that will accept the strin and integer the string has rotate anti clock wise
#    based on integer value?
# x='python'   a=int(intput("enter a val")
# class A:
#     def __init__(self,x,a):
#         self.x=x
#         self.a = int(input('enter a val:'))
#         for i in self.x:
#             if a==1:
#                 print(self.x[1:],end='')
#                 print(self.x[:a])
#                 break
#             if a==2:
#                 print(self.x[2:],end='')
#                 print(self.x[:a])
#                 break
#             if a==3:
#                 print(self.x[3:],end='')
#                 print(self.x[:a])
#                 break
# obj=A('python',1)
# obj=A('python',2)
# obj=A('python',3)
# o/p:-
# enter a val:1
# ythonp
# enter a val:2
# thonpy
# enter a val:3
# honpyt



#Q10. Create a class that will accept the string extract the numbers from string and convert remaining
#     string into ascci converted string?
# class Z:
#     def extract(self):
#         self.manu='A1B2c3'
#         for val in self.manu:
#             if val.isdigit():
#                 print(val,end='')
#         print()
#         for val in self.manu:
#             if val.isalpha():
#                 print(val,end='')
#         print()
#         for val in self.manu:
#             if val.isalpha():
#
#                 print(ord(val),end='')
# x=Z()
# x.extract()
# o/p:-
# 123
# ABc
# 656699