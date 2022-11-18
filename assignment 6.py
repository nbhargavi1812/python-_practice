# Q1.Find the length of the string without using length function?
# x=input('enter the string:')
# count=0
# for letter in x:
#        count+=1
# print(count)
# o/p:-
# enter the string:computer
#8

# Q2.x=1A2B3C  o/p:123ABC
# x=input('enter a value:')
# y=''
# z=''
# for i in x:
#        if i.isdigit():
#          y+=i
#        else :
#            if i.isalpha():
#                   z+=i
# print(y+z)
# O/P:-
# enter a value:1A2B3C
# 123ABC





# Q3.x=[1,0,0,1,0,1,0] o/p :0000111 in string format
# x=[1,0,0,1,0,1,0]
# x.sort()
# print(x)
# y=[str (i) for i  in x]
# a=str(''.join(y))
# print(a)
# o/p:-
# [0, 0, 0, 0, 1, 1, 1]
# 0000111

# Q4.x="hel$$lo#5#" o/p :hel$lo#5 remove only duplicates of special characters alone
# x="hel$$lo#5#"
# y=[]
# for i in x:
#        if i not in y:
#               y.append(i)
# print(y)
# y=' '.join(y)
# print(y)
# o/p:-
# ['h', 'e', 'l', '$', 'o', '#', '5']
# h e l $ o # 5


#
# 5.print the maximum character which is occur in given string
# ex: HELLLOPQ  o/p : maximum char in given string is L
# x=input("enter the string:")
# y=set(x)
# print(y)
# max=0
# for i in y :
#        if x.count(i)>max:
#               max=x.count(i)
#               print('max char is{} and count is{}'.format(i,max))
#
# # # O/P:-
# enter the string:HELLLOPQ
# {'O', 'E', 'H', 'P', 'Q', 'L'}
# max char isL and count is3


# Q6.x="hello python java is good"  count the number of words in given string and print output in below format
#    o/p :hello5 python6 java4 is2 good4
# x="hello python java is good"
# print(x.split())
# y=x.split()
# for i in range(len(y)):
#         y[i]+=str(len(y[i]))
#
# print(y)
# O/P:-
# ['hello', 'python', 'java', 'is', 'good']
# ['hello5', 'python6', 'java4', 'is2', 'good4']



# Q7.x='Hello javA Is Good' ...please make each word of first and last letter if it is upper make lower
#     if it is lower make upper   # o/p: 'hellO Java iS gooD'
# x='Hello javA Is Good'
# y=x.split()
# print(y)
# for i in range(len(y)):
#        if y[i][0].isupper():
#               x = x.replace(y[i][0], y[i][0].lower())
#        if y[i][0].islower():
#               x = x.replace(y[i][0], y[i][0].upper())
#        if y[i][-1].islower():
#               x = x.replace(y[i][-1], y[i][-1].upper())
#        if y[i][-1].isupper():
#               x = x.replace(y[i][-1], y[i][-1].lower())
# print(x)
# o/p:-
# ['Hello', 'javA', 'Is', 'Good']
# hellO Java iS gOOD



# Q8.x='hello java'  o/p : 'hello hello java java'
# x='hello java'
# y=x.split()
# print(y)
# y=[i*2 for i in y]
# print(y)
# y=' '.join(y)
# print(y)
# o/p:-
# ['hello', 'java']
# ['hellohello', 'javajava']
# hellohello javajava

#Q.9.swap commas to dots and dots to commas
#Input : 14, 625, 498.002
#Output : 14.625.498, 002
# x= '14, 625, 498.002'
# x=x.replace('14, 625, 498.002','14. 625.498, 002')
# print(x)


# Q10.x='12&&3AB$&+'   o/p :&&$&+ print only special characters from string
# x='12&&3AB$&+'
# numbers=''
# specialchar=''
# alpha=''
# for i in range(len(x)):
#        if (x[i].isdigit()):
#               numbers+=x[i]
#        elif(x[i].isalpha()):
#               alpha+=x[i]
#        else:
#               specialchar+=x[i]
# print(specialchar)
# o/p:-&&$&+

