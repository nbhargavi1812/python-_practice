# Q1. Write a function sum of given numbers pass 1,2,3 n return result is 6.
# def sum(x,y,z):
#     return x+y+z
# d=sum(1,2,3)
# print(d)
# o/p:-  6


# Q2. Write a function to print even & odd num in list?
# x=list(range(1,11))
# even=[]
# odd=[]
# def even_odd(x):
#     for i in range(len(x)):
#         if x[i]%2==0:
#             even.append((x[i]))
#         else:
#             odd.append((x[i]))
#     return even,odd
# y=even_odd(x)
# print(y)
# o/p:- ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])


# Q3.Write a program for default args and return result?
# def java(a,b,c='world'):
#     print('a val',a)
#     print('b val', b)
#     print('c val',c)
# java(14,63)
# o/p:-
# a val 14
# b val 63
# c val world

#
# Q4.Write a function to print multiplication table pass n from keyboard?
# def mul(n):
#     for i in range(1,11):
#         print(n,'*',i,'=',n*i)
# n=9
# mul(n)
# o/p:-
# 9 * 1 = 9
# 9 * 2 = 18
# 9 * 3 = 27
# 9 * 4 = 36
# 9 * 5 = 45
# 9 * 6 = 54
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81
# 9 * 10 = 90



#
# Q5. Write a function pass n of args & return list using variable len args?
# def fun(x,y,*z):
#     print(x)
#     print(z)
#     print(y)
# fun(7,8,9,4,5,6,1,2,3)
# o/p:-
# 7
# (9, 4, 5, 6, 1, 2, 3)
# 8

#
# Q6.  Write a function pass Keyword args & return dict(a=10,b=20,c=30)     o/p:-{a:100,b:400,c:900}
# def mul(a,b,c):
#     print('a val',a*a)
#     print('b val',b*b)
#     print('c val',c*c)
# mul(10,20,30)
# def java(**mul):
#     pr'int(mul)
# java(a=100,b=400,c=900)
# o/p:-
# a val 100
# b val 400
# c val 900
# {'a': 100, 'b': 400, 'c': 900}

#
# Q7. Write a function to fetch first word from list elements x=['PYTHON IS GOOD','JAVA IS GOOD']  O/P:-['PYTHON','JAVA']
# x=['PYTHON IS GOOD','JAVA IS GOOD']
# out=[]
# for i in range(len(x)):
#     temp=x[i].split()
#     out.append(temp[0])
# print(out)
# o/p:-
# ['PYTHON', 'JAVA']



# Q8.  Write a function to change string lower to upper & upper to lower &return the string?
# x='PYThon Is GOod'
# def low(a):
#     return a.swapcase()
# i=low(x)
# print(i)
# o/p:-
# pytHON iS goOD





# Q9.Write a function to get only vowels from the list
# # x=["PYTHON IS GOOd","JAVA IS GOOD"]   ->[I,O,I,O,O,A,A,I,O O]  -> remove the duplicates -> ['I','O','A']
# x=['PYTHON IS GOOD','JAVA IS GOOD']
# for i in range(len(x)):
#     vowels_list=['A','E','I','O','U']
# def list_data(vowels_list,x):
#     out=[]
#     y=''.join(x)
#     print(y)
#     for i in y:
#         if i in vowels_list and i not in out:
#             out.append(i)
#     return out
# dup=list_data(vowels_list,x)
# print('dup val:',dup)
# o/p:-
# PYTHON IS GOODJAVA IS GOOD
# dup val: ['O', 'I', 'A']


# Q10. Write a function to get max numbers from list without using predefined fun max ?
# x=[101,200,3000,400]
# def max(x):
#     max=x[0]
# for i in x:
#         if i>max:
#             max=i
#     return max
# x=[101,200,3000,400]
# print(max(x))
# o/p:-3000

#
# Q11. Write a function to sort the list without using sort fun   hint:use sorted fun
# x=[1,9,4,8,10,5]
# print(sorted(x))
# o/p:-
# [1, 4, 5, 8, 9, 10]



