# Q5.
# f=open('student.txt','w')
# f.write('python is good\n')
# f.write('java is good\n')
# f.write('all students are good\n')
# f.close()
# with open('student.txt','r+') as f:
#     text=f.read()
#     print(text)
#     print('the current cursor position:', f.tell())
#     f.seek(0)
#     print('the current cursor position:', f.tell())
#     f.write('PYTHON')
#     f.seek(0)
#     text = f.read()
#     print(text)
#     print('the current cursor position:',f.tell())
#     f.seek(10)
#     print('the current cursor position:',f.tell())
#     f.write('GOOD')
#     f.seek(0)
#     text=f.read()
#     print(text)
#     print('the current cursor position:', f.tell())
#     f.seek(16)
#     print('the current cursor position:', f.tell())
#     f.write('JAVA')
#     f.seek(0)
#     text = f.read()
#     print(text)
#     print('the current cursor position:', f.tell())
#     f.seek(24)
#     print('the current cursor position:', f.tell())
#     f.write('GOOD')
#     f.seek(0)
#     text = f.read()
#     print(text)
#     print('the current cursor position:', f.tell())
#     f.seek(30)
#     print('the current cursor position:', f.tell())
#     f.write('ALL')

#     f.seek(0)
#     text = f.read()
#     print(text)
#     print('the current cursor position:', f.tell())
#     f.seek(47)
#     print('the current cursor position:', f.tell())
#     f.write('GEMS')
#     f.seek(0)
#     text = f.read()
#     print(text)
#     f.close()
#
# f2=open('sample2.py','w')
# f2.write(text)
# print(f2)
# f.close()
#o/p:-
# PYTHON is GOOD
# JAVA is GOOD
# ALL students are GEMS



# Q7.
# data='python is good'
# f=open('student1.txt','w')
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


# Q10.
f=open('sample.txt','w')
f.write('HELLO FRIENDS')
f.close()
with open('sample.txt','w+') as f:
    hi=f.read()
    print(hi)
    f.write('HELLO FRIENDS')
