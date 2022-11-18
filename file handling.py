# f=open('bhargavi.file','r')
# print(f.read())
# f.close()
import os.path
import sys

# creating a file:
# import os
# fname='bhargavi.file'
# f=open('bhargavi.file','w')
# print('open bhargavi file')
# f.close()



# To check the file and read & write also:
# import os.path
#
# if os.path.exists('bhargavi.file'):
#     f=open('bhargavi.file','r')
#     x=f.readlines()
#     print(x)
#     f.close()
# else:
#     print('file not exists')
#     f=open('bhargavi.file','w')
#     f.close()


# To append :
# f=open('bhargavi.file','a')
# f.write('shall we join\n')
# f.write('together\n')
# f.close()


# To r+:
# f=open('bhargavi.file','r+')
# print(f.read())
# f.write('for discussion')
# f.close()


# To w+:
# f=open('bhargavi.file','w+')
#
# f.write('of doubts in covered topics')
# f.seek(4)
# f.seek(6)
# print(f.read())
# f.close()

# To a+:
# f=open('bhargavi.txt','a+')
# f.write('welcome\n')
# f.seek(5)
# print(f.read())
# f.close()

# To x:
# f=open('python.file','x')
# print('is file there')
# f.close()



# To r in binary:
# with open('bhargavi.file','rb') as f:
#      print(f.read())
#
#


# #In binary:
# f=open('bhargavi.txt','r+b')
# print(f.read())
# f.close()

#
# reading character data from txt files:
# f=open('txt.files','x')
# print('as file created')
# f.close()
# y=('hi\n','hello\n','how r u doing\n')
# f=open('txt.files','w')
# f.writelines(y)
# f.close()
# f=open('txt.files','r')
# lines=(f.readlines())
# print(lines,end=' ')
# line3=(f.readline())
# print(line3,end=' ')
# line8=(f.readline())
# print(line8,end=' ')
# f.close()


# in write lines:
# x=['pretheka\n','shivaansh\n']
# f=open('bhargavi.txt','w+')
# f.writelines(x)
# f.seek(5)
# print(f.read())
# f.close()
#
# PROPERTIES OF FILE OBJECT:
# f=open('bhargavi.txt','r')
# print('file name:',f.name)
# print('mode:',f.mode)
# print('is file readable:',f.readable())
# print('is file can writeable:',f.writable())
# print('is file closed:',f.closed)
# f.close()
# print('is file closed:',f.closed)


# seek and tell:
# f=open('bhargavi.txt','w+')
# f.write('hello\n')
# f.seek(4)
# # print(f.read())
# f.close()
# f=open('bhargavi.txt','r')
# # print(f.tell())
# print((f.read(3)))
#
# print(f.tell())
# f.seek(0)
# print(f.read(2))
# print(f.tell())
# print(f.tell())
# print(f.read(3))
# print(f.tell())
# print(f.read(4))
# print(f.tell())


# To change the data:
# data='java is good'
# f=open('abc.txt','w')
# f.write(data)
# f.close()
# with open('abc.txt','r+') as f:
#      text=f.read()
#      print(text)
#      # print('the current cursor position:',f.tell())
#      # f.seek(13)
#      print('the current cursor position:',f.tell())
#      f.write('HELLO FRIENDS')
#      f.tell()
#      print('the current cursor position:', f.tell())
#      f.seek(0)
#      text=f.read()
#      print('data after modification')
#      print(text)


#import os ,sys:
# fname='bhargavi.txt'
# if os.path.exists(fname):
#      print('file exists:',fname)
#      f=open(fname,'r')
#      print(f.readlines())
# else:
#      print('file does not exists:',fname)

#      sys.exit(0)


#image:

# f1=open('pretheka.JPG','rb')
# bytes=f1.read()
# print(bytes)
# f1.close()
# f2=open('pretheka rephoto.JPG','wb')
# f2.write(bytes)
# print('new image')
# f2.close()

#
# f1=open('shivaansh.JPG','rb')
# bytes=f1.read()
# print(bytes)
# f1.close()
# f2=open('shivanshimage.JPG','wb')
# f2.write(bytes)
# print('new image')
# f2.close()


#CSV:
# import csv
# with open('emp.csv','w',newline='') as f:
#     w=csv.writer(f)
#     w.writerow(['eno','ename','esal'])
#     n=int(input('enter no.of employees:'))
#     for i in range(n):
#         x=[]
#         eno=input('enter empl no:')
#         x.append(eno)
#         ename = input('enter empl name:')
#         x.append(ename)
#         esal= input('enter empl sal:')
#         x.append(esal)
#         w.writerow([eno,ename,esal])
#         print('total employees data to csv file')