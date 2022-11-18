# print('python')
# print(10/'ten')

#control flow
# try:
#     print('statics')
#     print(10/0)
#     print('java')
# except ValueError as e:
#
#      print(e)
#      print('sample')
# except ZeroDivisionError as e:
#      print(10/0)
#      print('null')


# by alias name:
# try:
#     print('alaska')
#     print(10/0)
# except ZeroDivisionError as hi:
#     print(hi)
#     print('deserts')

#try by multiple except blocks:
# try:
#     x=int(input('enter first number:'))
#     y=int(input('enter second number:'))
#     print(x/y)
#     print('caterpillar')
# except Exception as e:
#      print('cocoon')
# except ZeroDivisionError  as wings:
#       print('pls provide int value only')


#single except block but multiple exceptions:
#1.  try:
#     print('umbrella')
#     print(10/0)
#     print('rain coats')
# except (ZeroDivisionError,ValueError,TypeError)   as rainy:
#     print(rainy)
#     print('as it is which error')



# #2.
# try:
#      x=int(input('enter first number:'))
#      y=int(input('enter second number:'))
#      print(x/y)
# except (ZeroDivisionError,ValueError)   as q:
#     print(q)
#     print('pls provide valid error nos only &problem is :',q)


#default except block:
# try:
#     x=int(input('enter first number:'))
#     y= int(input('enter second number:'))
#     print(x/y)
#     print('hi')
#
# except:
#     print('default :plz provide input only')

# #combinations by final blocks:
# import os
# try:
#     print(10-20)
#     print(10/0)
#     # os._exit(0)
#     print('hi')
# #     os._exit(0)
# except Exception as e:
#     # os._exit(0)
#     print('except')
#     os._exit(0)
#     print('gp')
# finally:
#    print('marks')






#nested exception
# try:
#     print('outer try ')
#     print(10/2)
#     print('hi')
#     try:
#         print(10/0)
#         print('inner try')
#     # except Exception as e:
#     #     print(e)
#     except(ZeroDivisionError,ValueError)   as l:
#         print(l)
#         print(' inner except:',l)
#     finally:
#         print('inner final')
# # except Exception as e:
# #     print('outer except')
# except(ZeroDivisionError,ValueError) as l:
#     print('outer l')
# finally:
#     print('outer final')


#else part:

















































































































































































































































































