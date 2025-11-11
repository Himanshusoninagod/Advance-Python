# on the basis of arguement and return 
# Type of function - 
# 1. with arguement and with return 
# 2. with arguement and without return 
# 3. without arguement and with return 
# 4. without arguement and without return 


# Example- 
# 1. with arguement and with return 

# def show_detail(name):
#     return name

# x= input("enter your name: ")
# result= show_detail(x)
# print(result)
# print(show_detail(x))


# 2. with arguement and without return-

# def sum(a,b):
#     print(a+b)

# x=int(input("enter value of a: "))
# y=int(input("enter value of b: "))
# sum(x,y)


# 3. without arguement and with return -

# def sum():
#     a=int(input("enter value of a: "))
#     b=int(input("enter value of b: "))
#     return (a+b)

# result = sum()
# print(result)


# 4. without arguement and without return -

# def show_name():
#     print("Himanshu")

# show_name()



# variable Scope -

# x,y = 10,20
# def add():
#     p,q = 30,40
#     print(x,y)
#     print(p,q)
# add()
# print(x,y)
# print(p,q)  # error

# x,y = 10,20
# def add():
#     x=10
#     print(x)
# add()
# print(x)


# x,y = 10,20
# def add():
#     x=20
#     print(x)
# add()
# print(x)


# Define global variable - 

# x,y = 10,20
# def add():
#     global z
#     z=20
#     print(z) 
# add()   
# print(z)


# x=10
# def add():
#     x=20
#     print(globals()['x']+x)
# add()
# print(x)









