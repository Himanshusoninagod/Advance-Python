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