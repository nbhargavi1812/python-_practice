# # Q7.
# x={'A':[1,2,3],'B':[4,5,6]}
# out={}
# keys=list(x.keys())
# print(keys)
# for i in x.keys():
#     temp=x[i]
#     temp.reverse()
#     out[i]=temp
#     print(out)
# O/P:-
# ['A', 'B']
# {'A': [3, 2, 1]}
# {'A': [3, 2, 1], 'B': [6, 5, 4]}




# Q8. x='Hello PYTHON who ARE YOU'   O/P:-  {'H': 'HELLO', 'P': 'PYTHON', 'W': 'WHO', 'A': 'ARE', 'Y': 'YOU'}
# x='Hello PYTHON who ARE YOU'
# x=x.upper()
# print(x)
# keys=[]
# values=[]
# x=x.split()
# for i in range(len(x)):
#     keys.append(x[i][0])
#     values.append(x[i])
# out=dict(zip(keys,values))
# print(out)






# if___name___='___main__':
# Q9.
# x={'c1':[10,20,30],'c2':[20,30,40],'c3':[12,34]}
# out={}
# keys=list(x.keys())
# values=list(x.values())
# for i in range(len((values))):
#     values[i].reverse()
# print(values)
# out=dict(zip(keys,values))
# print(out)
# o/p:-
# [[30, 20, 10], [40, 30, 20], [34, 12]]
# {'c1': [30, 20, 10], 'c2': [40, 30, 20], 'c3': [34, 12]}.


 # Q10
# x={1:'red',2:'green',3:'white',4:'black'}
# out={}
# for i in x.values():
#     out[i]=len(i)
# print(out)
# o/p:-{'red': 3, 'green': 5, 'white': 5, 'black': 5}
#
#



# Q5
# .x={'A':3,'B':5,'C':4,'D':2,'E':1}   O/P:-Ascending order of values
# x={'A':3,'B':5,'C':4,'D':2,'E':1}
# out={}
# out=dict(sorted(x.items()))
# print(out)
# i=list(x.keys())
# j=list(x.values())
# z=dict(zip(j,i))
# print(z)
# p=dict(sorted(z.items()))
# print(p)
# i=list(p.keys())
# j=list(p.values())
# z=dict(zip(j,i))
# print(z)
# o/p:-
# {'A': 3, 'B': 5, 'C': 4, 'D': 2, 'E': 1}
# {3: 'A', 5: 'B', 4: 'C', 2: 'D', 1: 'E'}
# {1: 'E', 2: 'D', 3: 'A', 4: 'C', 5: 'B'}
# {'E': 1, 'D': 2, 'A': 3, 'C': 4, 'B': 5}
