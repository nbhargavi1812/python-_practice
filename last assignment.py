#Q1. What are the modes in file handling? What are they?
#A. 1.r-> It will open an existing file and the data.If the file doesn't exits then by default it gives file not found.
#   f=open("photos.txt",'r')
#   print(f.read())
#   f.close()
# 2.w-> It will open the existing file & write.
#    ->If already file exists then it will overridden the data.
#    ->If file not found it will create.
#   f=open("photos.txt",'w')
#   print("file is created")
#   f.close()
# -> To check the import os.path.exists(fname)
# 3. a-> It will open the existing file for append operation.
#    -> It  won't override the existing data ,if file not there it will create.
#   f=open('photos.txt','a')
#   f.write('shall we join\n')
#   f.close()
# 4. r+-> It will read and write data into the file,previous data will not  be deleted.
#   f=open('photos.txt','r+')
#   print(f.read())
#   f.write('for discussion')
#   f.close()
# 5. w+-> To write and read data,it will override the existing data.
# f=open('photos.txt','w+')
# f.write('of doubts in covered topics')
# f.seek(4)
# f.seek(6)
# print(f.read())
# f.close()
# 6. a+-> To append and read data,it will override the existing data.
#   f=open('photos.txt','a+')
#   f.write('welcome\n')
#   f.seek(5)
#   print(f.read())
#   f.close()
# 7. x-> To open a file in exclusive mode for write operation.If file already exists it gives error.
#     -> for this file creation we have to import os
# import os
# f=open('python.file','x')
# print('is file there')
# f.close()


#Q2. How to create a file? How many ways we can create the file?
#A.  for only file creation we can use x mode or we can use inbuilt function open.
#   In 4 ways we can create the file.
#   They are: 1.w mode
#             2.a mode
#             3.w+ mode
#             4.a+ mode


#Q3. Extract the key words from python file?


#Q4. What are decorator,generator,iterator with example?
#A. Decorator: Without touching extisting functionality adding new features to the function is called decorator.
#  example:
# def diamonds(fun):
#     print('use in ornaments')
#     fun()
#     def siver():
#         print('uesd daily')
#         fun()
#     return siver()
# @ diamonds
# def gold():
#     print('all glitters are not gold')
# o/p:-
# use in ornaments
# all glitters are not gold
# uesd daily
# all glitters are not gold

# Generator:It is a function which is used to generate the sequence of values.
# ->It contains yeild keyword to return values.
# ->generator by default having iterator and __next__()
# def reliance():
#     yield 'x'
#     yield 'y'
#     yield 'z'
# g=reliance()
# for i in g:
#     if i=='y':
#         print(i)
#         break
#
# print(next(g))
# o/p:-
# y
# z

Iterator: