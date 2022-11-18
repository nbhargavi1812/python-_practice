

#
# data='All Students are Good'
# f=open('bhargavi.txt','w')
# f.write(data)
# f.close()
# with open('bhargavi.txt','r+') as f :
#     text=f.read()
#     print(text)
#     print('the current cursor position:',f.tell())
#     f.seek(17)
#     print('the current cursor position:', f.tell())
#     f.write('GEMS!!!')
#     f.seek(0)
#     text=f.read()
#     print('data after modification')
#     print(text)



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





#
#
# # Q7.
# data='python is good'
# f=open('student.txt','w')
# f.write(data)
# # f.write('java is good\n')
# # f.write('all students are good\n')
# f.close()
# with open('student.txt','w+') as f:
#     text=f.read()
#     print(text)
#     print('the current cursor position:', f.tell())
#     f.seek(0)
#     print('the current cursor position:', f.tell())
#     f.write(("HELLO FRIENDS"))
#     f.seek(0)
#     text = f.read()
#     print(text)
#     f.close()
#

# x=[1,2,3,4]
# import functools
# output=[]
# for i in range(len(x)):
#     if i>=0:
#         d=[]
#         d.extend(x[:i]+x[i+1:])
#         out=functools.reduce(lambda a,b:a*b,d)
#         output.append(out)
# print(output)

#
#
# x=[-7,-3,-2,-1]
# import functools
# output=[]
# for val in range(len(x)):
#     if val>=0:
#         d=[]
#         d.extend(x[:val]+x[val+1:])
#         out = functools.reduce(lambda a, b: a * b, d)
#         output.append(out)
# print(output)


# assignment
# data='HELLO FRIENDS'
# f=open('sample.txt','w')
# f.write('HELLO FRIENDS')
# f.close()
# with open('sample.txt','w+') as f:
#      text=f.read()
#      print(text)
#
#      print('the current cursor position:', f.tell())
#      f.seek(0)
#      print('the current cursor position:', f.tell())
#      f.write('FRIENDS')
#      f.seek(0)
#      text = f.read()
#      print(text)
#      text = f.read()
#      print(text)
#      print('the current cursor position:', f.tell())
#      f.seek(8)
#      print('the current cursor position:', f.tell())
#      f.write('HELLO')
#      f.seek(0)
#      text = f.read()
#      print(text )
     # print('the current cursor position:', f.tell())
     # f.seek(0)
     # print('the current cursor position:', f.tell())
     # f.write('FRIENDS')
     # f.seek(0)
     # text = f.read()
     # print(text)
# f2=open('sample.txt','w')
# f2.write(text)
# print(
# #
# f.close()

# # last ass Q10.
f=open('assignment.txt','w')
f.write('HELLO FRIENDS\n')
# f.write('HI STUDENTS\n')
print('file is created')
f.close()
f1=open('output.txt','w')
with open('assignment.txt','r+')as myfile:
     data=myfile.read()
     print(data[-1::-1])
     myfile.seek(6)
     print(myfile.read(7))
     print(myfile.tell())
     f.write(myfile)
     myfile.seek(0)










