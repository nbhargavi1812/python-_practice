#Q1.what is tuple and set ? write difference between them ?
# A. Tuple:-1.Tuple is exactly same as List.But tuple is immutable.
#    2. If our data is fixed and never changes then we should go for Tuple.
# Set:-Set is a group of unique values and this is mutable.
# ________________________________________________________________________________________________
# |___________________TUPLE________________________|___________________SET________________________|
# |we cannot change the values.                    |     we cannot change the values.             |       |
# |                                                |                                              |
# |Duplicates are allowed.                         |     Duplicates are not allowed.              |
# |                                                                                               |
# |Insertion Order is preserved.                   |     Insertion order is not preserved.        |
# |                                                                                               |
# |Indexing and slicing is allowed.                |      Indexing and slicing not allowed.       |
# |                                                                                               |
# |x=tuple()                                       |      x=set()                                 |
# ________________________________________________________________________________________________|



#Q2.what is set comprehension ? write an example?
# A.set comprehension:The operstions which we are doing inside the set is called set comprehension.
#Example:
# x= {i for i in range(1,11)  if i%2!=0}
# print(x)
# o/p:-{1, 3, 5, 7, 9}
# y={i**2 for i in range(1,11)}
# print(y)
# o/p:-{64, 1, 4, 36, 100, 9, 16, 49, 81, 25}


#Q3.x=[1,4,5,3,1,4] reverse the list and remove the duplicates using set ?
# x=eval(input("enter the values in the list:"))
# y=set(x)
# print(type(y))
# print(y)
# o/p:-
# enter the values in the list:[1,4,5,3,1,4]
# <class 'set'>
# {1, 3, 4, 5}

#Q4.Take two sets get unique values from set ?
# x={1.0j,3,0.5,6.0}
# y={2.8,4,6.0,0.5,1.0j}
# print((x.intersection(y)))
# o/p:-{0.5, 1j, 6.0}

#Q5.How to concatinate two sets ? write an example?
#A. We can concatiante two sets by add(+) two sets.
#Example:
# x={1.5,2.0,3.5j}
# y={0.2,4,6.6,5,1}
# print(x.union(y))
# o/p:-{0.2, 1.5, 2.0, 1, 4, 5, 6.6, 3.5j}


#Q6.write a program to get  common elements from  two sets ?
# x={1,3,5,6,9,10,2}
# y={2,4,6,5,1,7}
# print(x.intersection(y))
# o/p:-{1, 2, 5, 6}

#Q7.write a example for tuple comprehension ?
#A.Tuple comprehension:The operations which we are doing inside the tuple is called tuple comprehension.
# y=(i**2 for i in range(1,8))
# print(y)
# for x in y:
#    print(x,end=' ')
# o/p:-
# <generator object <genexpr> at 0x000001FB137D2490>
# 1 4 9 16 25 36 49

#Q8.x=[6,3,2,5,1]  sort the list elements without using sort function ? op : [1,2,3,5,6]
# x=[6,3,2,5,1]
# print(sorted(x,reverse=False))
# O/P:-[1, 2, 3, 5, 6]


#Q9.write a program to change tuple values using list ?
# x=(0,1,1.2,3,4.0)
# y=list(x)
# print(y)
# y[1]=5
# print(y)
# y[4]=8
# print(y)
#
# # o/p:-
# [0, 1, 1.2, 3, 4.0]
# [0, 5, 1.2, 3, 4.0]
# [0, 5, 1.2, 3, 8]

# Q10.print the multiplication table using loops ->
# input should be taken from keyboard ?
# A.  16*1=16
# x=int(input("multiplication table:"))
# for i in range(1,11):
#     print(x,'*',i,'=',x*i)
# o/p:-
# multiplication table:16
# 16 * 1 = 16
# 16 * 2 = 32
# 16 * 3 = 48
# 16 * 4 = 64
# 16 * 5 = 80
# 16 * 6 = 96
# 16 * 7 = 112
# 16 * 8 = 128
# 16 * 9 = 144
# 16 * 10 = 160
