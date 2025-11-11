# def add_all(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(sum)

# add_all(10,20,30,40,50)

# def add_all(*n):
#     sum=0
#     for i in n:
#         print(i) 
#         for j in i:
#             sum=sum+j
#     # print(f'sum is {sum}') 

# var = eval(input("enter any collection:"))
# add_all(var)



# def add_all(*n):
#     print(n)

# var = eval(input("enter any collection:"))
# add_all(*var)


# def add_all(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(f'sum is {sum}')

# var = eval(input("enter any collection:"))
# add_all(*var)


# error case- 

# 1. 
# def display(x=0,y):
#     print(f'{x,y}')
# diaplay(10,20)

# 2. 
# def display(*n,x):
#     print(f'{n,x}')
# display(10,20,30)




# def display(x,y=0,*z):
#     print(f'{x,y,z}')
# display(10,20,30,40,50)

# def display(p,q,r=0,*s):
#     print(f'{p,q,r,s}')
# display(10,20,30,40,50)


# 4. Keyword arguement - 

# def fun_name(x,y,z):
#     print(f'{x,y,z}')

# fun_name(y=10,x=5,z=3)



# 5. Default Keyword Arguement -

# a. for empty- 
# def fun_name(x=0,y=0,z=0):
#     print(f'{x,y,z}')

# fun_name()

# b. pass only 2 values- 
# def fun_name(x=0,y=0,z=0):
#     print(f'{x,y,z}')

# fun_name(x=10,y=20) 

# c. pass extra values- 
# def fun_name(x=0,y=0,z=0):
#     print(f'{x,y,z}')

# fun_name(x=10,y=20,z=30,a=40) 



# 6. Variable-Length Keyword arguement -

# def fun_name(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
        
# fun_name(x=10,y=20,z=30,p=2,q=6,r=10)


# def fun_name(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
        
# var = eval(input("enter any Dictonary: "))        
# fun_name(**var)



# def fun_name(**n):
#     for k,v in n.items():
#         print(f'{k}={v}')
        
# var = eval(input("enter any Dictonary: "))        
# fun_name(**var)












