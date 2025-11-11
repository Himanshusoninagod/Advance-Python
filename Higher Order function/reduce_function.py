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