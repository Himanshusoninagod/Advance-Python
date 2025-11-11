# Higher Order Function - 

# 1. Map Function - map() 

# syntex - 
# map(fun_name, collection)

# li = [1,2,3,4,5]
# def square(n):
#     return n*n
# result = map(square,li)
# print(result)
# print(list(result))


# syntex - 
# map(fun_name, collection1,collection2,collection3) 

# l1=[1,3,5,7]
# l2=[1,2,3]
# l3=[1,2,3,4,5,6,7]
# def add(x,y,z):
#     return x+y+z
# result = list(map(add, l1,l2,l3))
# print(result)


# 2. Filter function - filter()

# Syntex - 

# collection/iterator 
# def fun_name(x):
#     fun_body
# reesult = filter(fun_name, collection/iterator)

# l = [1,2,3,4,5]
# def even(n):
#     if n%2==0:
#         return n
# result = list(filter(even, l))
# print(result)


# l = [1,2,3,4,5]
# def even(n):
#     if n%2==0:
#         return 'even'
#     else :
#         return 'odd'
# result = list(map(even, l))
# print(result)


# 3. Reduce function - reduce() 

# Syntex - 

# import functools
# collecton/iterator
# def fun_name(x,y):
#     fun_body
# result = functools.reduce(fun_name, iterator)
# result = functools.reduce(fun_name, iterator, initial_value(optional))

# import functools
# l = [1,2,3,4,5,6]
# def add(x,y):
#     return x+y
# result = functools.reduce(add, l)
# print(result)

# first it takes 2 values 1 and 2 then add both values then take single value and add 


# from functools import reduce
# l = [10,2,5,20,6,9]
# def max(x,y):
#     if x>y:
#         return x
#     else :
#         return y
# result = reduce(max, l)
# print(result)

# from functools import reduce
# l = [10,2,5,20,6,9]
# def min(x,y):
#     if x<y:
#         return x
#     else :
#         return y
# result = reduce(min, l)
# print(result)


# 4. Lambda function - lamda()

# lambda parameters:expression 

# p = lambda x,y:print(x+y) 
# p(4,5) 
# print(p(3,4)) 

# z = p(4,5) 
# print(z)


# square of list function - 

# using mapm function -

# l = [1,2,3,4,5]
# def sqar(n):
#     return n*n
# result = list(map(sqar, l))
# print(result)


# using lambda function - 

# l = [1,2,3,4,5]
# print(list(map(lambda n:n*n, l)))
     

# l1 = [1,2,3,4,5]
# l2 = [2,4,6]
# l3 = [1,8,6,4,3,8]
# print(list(map(lambda x,y,z:x+y+z, l1,l2,l3)))


# using filter function - 

# l = [1,2,3,4,5]
# def even(n):
#     if n%2==0:
#         return n
# result = list(filter(even, l))
# print(result)


# using lambda function - 

# l = [1,2,3,4,5,6,7,8]
# print(list(filter(lambda n:n if n%2==0 else None, l)))
# print(list(filter(lambda n:n%2==0, l)))


# using map() function -

# l = [1,2,3,4,5]
# def even(n):
#     if n%2==0:
#         return 'even'
#     else :
#         return 'odd'
# result = list(map(even, l))
# print(result)


# using lambda function - 

# l = [1,2,3,4,5,6,7,8]
# print(list(map(lambda n:'even' if n%2==0 else 'odd', l)))


# import functools
# l=[1,2,3,4,5,6,7,8]
# print(functools.reduce(lambda x,y:x+y, l)) 

# max value -
# print(functools.reduce(lambda x,y:x if x>y else y, l)) 

# min value -
# print(functools.reduce(lambda x,y:x if x<y else y, l)) 


# list comprehention
# set comprehention
# dict comprehention

# 5. Decorator - 

# def outer(x):
#     def inner():
#         print("welcome")
#         x()
#     return inner

# def display():
#     print("Hello")

# res = outer(display)
# res()


# def outer(x):
#     def inner():
#         print("welcome")
#         x()
#     return inner

# @outer
# def display():
#     print("Hello")

# display()



# def outer(x):
#     def inner(p,q):
#         p=p+5
#         q=q+10
#         x(p,q)
#     return inner
# @outer
# def display(x,y):
#     print(x+y)

# display(10,20)