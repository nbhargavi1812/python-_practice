#LIST
# a=[]
# a=list
# numbers=[1,3,5,7,9]
# print(type(numbers))
# q="pretheka"
# q=q.split()
# print(q)
# print(type(q))
#
# #ACCESSING THE ELEMENTS:
# a=['s','h','i','v','a','n','s','h']
# print(type(a))
# print(a[0:-1])
# print(a[-7:-2])
#
# #append:
# q=[1,3,5]
# q.append(4)
# print(q)
#
# #count
# q=[1,3,5,4,6,3,7,2,7,4]
# print(q.count(3))
#
# #index
# q=[1,2,5,6,8]
# print(q.index(8))
#
# #append
# flowers=['rose']
# print(flowers)
# flowers.append('hibiscus')
# print(flowers)
#
# #insert
# flowers.insert(0,'lily')
# print(flowers)
#
# #extend
# animals_voices=[]
# animals=['cat','dog','cow']
# sounds=['meow','bow','moo']
# animals_voices.append(animals)
# animals_voices.append(sounds)
# print(animals_voices)
# print(animals_voices[1][2])
#
# #remove
# flowers.remove('rose')
# print(flowers)
#
# #length
# print(len(flowers))
# print(len(a))

#reverse
# list=[10,11,12,14,13,15]
# list.reverse()
# print(list)
# new_list=list[::-1]
# new_list.reverse()
# print(new_list)
# l=[]
# for i in list:
#     l.insert(0,i)
# print(l)
# l.reverse()
# print(l)
# lis=['a','d','c','c','a','b','a','b','d','c','e']
# occurence={item:lis.count(item) for item in lis}
# print(occurence.get('c'))


#loops
# name="bhargavi nidamanuri"
# print(len(name))
# numbers=[20,30,20,40,50]
# for val in numbers:
#     print(val)
#
# # range:
# for i in range (1,18):
#     print(i,end=' ')

#odd numbers:
# for i in range(1,21,2):
#     print(i,end=' ')

#even numbers:
# for val in range(0,17,2):
#     print(val,end=' ')

#vowels:
# vowels=['a','e','i','o','u']
# # vowels={}
# print(type(vowels))
# print(vowels)
# for val in vowels:
#     print(val,end=


#DICTIONARY:
# Q1. Write a Python script to add a key to a dictionary.
# sample_Dictionary = {0: 10, 1: 20}
# sample_Dictionary[2]=30
# print(sample_Dictionary)
#Q2. Write a Python script to concatenate following dictionaries to create a new one
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic1.update({3:30, 4:40})
# print(dic1)
# dic1.update({5:50,6:60})
# print(dic1)
#Q3. Write a Python script to check whether a given key already exists in a dictionary.
# d={1:'a',2:'b',3:'c'}
# d[4]='d'
# d[5]=''
# print(d.keys())
# for k in d.keys():
#     print(k)
# for v in d.values():
#     print(v)
# for k,v  in d.items():
#     print(k,"-",v)

#Q4. Write a Python script to generate and print a dictionary that contains a number
# (between 1 and n) in the form (x, x*x)
# x={i:i*i for i in range(1,6)}
# print(x)

#Q5. x={i:i*i for i in range(1,16)}
# print(x)

#Q6.Write a Python program to remove a key from a dictionary
# d = {1: 'a', 2: 'b', 3: 'c'}
# print(d.get(1))
#Q7.Write a Python program to remove duplicates from Dictionary
# d={1:'q',2:'w',3:'e',3:'f',3:'f'}
# print(d)
# d.update({3:'r'})
# print(d)
#Q8.Write a Python program to check a dictionary is empty or not.
# d={1:'good',2:'better',3:'best',4:'worse'}
# d.pop(4)
# print(d)
# d.update({5:'vgood'})
# print(d)
# d.clear()
# print(d)
#Q9.
























# a='one'
# b='one'
# print(id(a))
# print(id(b))
# print(a is b)
#
# from math import factorial
# print(factorial(5))
#
# # area of circle=pie r 2
# from math import pi
# r=16
# print('area of circle=',pi*r**2)
#
# x=int(input('enter first number:'))
# y=int(input('enter second number:'))
# print('the sub of 2 num:',x-y)

# eno=int(input('enter employee number:'))
# ename=(input('enter employee name:'))
# esal=float(input('enter employee salary:'))
# eadd=int(input('enter employee address:'))
# estatus=bool(input('enter employee married?[true],[false]:'))
# ephno=int(input('enter employee phone num:'))
# print("details created successfully...!")
# print('employee number:',eno)
# print('employee name:',ename)
# print('employee salary:',esal)
# print('employee address:',eadd)
# print('employee married?[true],[false]:',estatus)
# print('employee phone num:',ephno)
#
# a,b=[list(x) for x in input('enter 2 string values:') .split(',')]
# print('the str:',a+b)

# print("Hello"+"World")
# print("Hello","World")

# a,b,c=1,2,3
# print(a,b,c,sep=':')


# a="friends"
# b="50"
# c="is"
# d="20"
#
# print("hello",a,"jai","crossed",b)
# print("janu",c,d)




# a="project"
# b=3.0
# c=2022
# # print("python %s.....is done in %f python charm %d"%(a,b,c))

# name="friends"
# value=25000
# print("hi {0} i got placed with package{1}".format(name,value))
#
# name="surya"
# year=2022
# name2="jyothika"
# print("{x} and{y} won national award in  {z} ".format(x=name,y=name2,z=year))



#
# n1=int(input("Enter First Number:"))
# n2=int(input("Enter Second Number:"))
# n3=int(input("Enter Third Number:"))
# if n1>n2 and n1>n3:
#     print("Biggest Number is:",n1)
# elif n2>n3:
#     print("Biggest Number is:",n2)
# else :
#     print("Biggest Number is:",n3)

# smallest of 2 numbers
# x=eval(input('enter first number'))
# y=eval(input('enter second number'))
# if x<=y:
#     print('small number',x)
# elif x>=y:
#     print('small number',y)
# else:
#     pass

# smaller from 3 numbers
# x=eval(input('enter first number'))
# y=eval(input('enter second number'))
# z=eval(input("enter third number"))
# if x<=y and x<=z:
#     print('small number',x)
# elif x>=y:
#     print('small number',y)
# elif y<=z:
#     print('small number',z)
# else:
#     pass


# Write a program to check whether the given number is even or odd?
# n=int(input("Enter Number:"))
# if n%2==0:
#     print('the number ',n,' is even')
# else:
#     print('the number',n,'is not even')

# To print Hello 10 times
for x in range(1,11) :
  print("Hello",end=' ')