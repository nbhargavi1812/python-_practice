# to find the Max of three numbers
# def funct():
#     x=10,-50,0.90
#     print(max(x))
# funct()

# sum all the numbers in alist
# def sum(a,b,c,d,e):
#      return a+b+c+d+e
# x=sum(a=8, d=2, c=3,b= 0,e=7)
# print(x)

# multiply all the numbers in a list
# def mul(a,b,c,d,e):
#     return a*b*c*d*e
# out=mul(8, 2, 3, -1, 7)
# print(out)

# reverse a string.
# def string():
#     x= "1234abcd"
#     print(x[::-1])
# string()

# calculate the factorial of a number
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# n = int(input("Input a number to compute the factiorial : "))
# print( factorial(n))

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case
# letters.
# def string(x):
#     d ={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in x:
#       if c.isupper():
#         d["UPPER_CASE"]+=1
#       elif c.islower():
#         d["LOWER_CASE"]+= 1
#       else:
#         pass
#     print("No. of Upper case characters :", d["UPPER_CASE"])
#     print("No. of lower case characters :", d["LOWER_CASE"])
# string('The quick Brown Fox')

# takes a list and returns a new list with unique elements of the first list.
# q=[1,2,3,3,3,3,4,5]
# def list(q):
#     l=[]
#     for i in q:
#         if i not in l:
#             l.append(i)
#     return l
# print(list([1,2,3,3,3,3,4,5]))

# takes a number as a parameter and check the number is prime or not
def number(x):
    n={'prime':0,'not prime':0}
    for i in x:
        if i%i==1:
            print("prime:",n['prime'])
        elif i%i!=1:
            print("not prime:", n['prime'])
        else:
            pass

print(number(9))