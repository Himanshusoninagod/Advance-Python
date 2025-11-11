# Decorator -

# Syntex -
# def decor (fun_name):
#     def new_function():


#     return new_function

# def add(x,y):
#     return x+y
# x = decor(add)

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


# def decorator(x):
#     def inner(p,q,r):
#         p=p+5
#         q=q+10
#         r=r+15
#         z=x(p,q,r)
#         return z 
#     return inner
# @decorator
# def add(a,b,c):
#     return a+b+c
# res = add(2,4,6)
# print(res)

# def decor(x):
#     def inner(p,q,r):
#         p=p+1
#         q=q+1
#         r=r+1
#         z=x(p,q,r)
#         return z
#     return inner
# @decor
# def multi(a,b,c):
#     return a+b+c
# res=multi(1,2,3)
# print(res)

# or 

# def decor(x):
#     def inner(p,q,r):
#         p=p+1
#         q=q+1
#         r=r+1
#         x(p,q,r)
#     return inner
# @decor
# def multi(a,b,c):
#     print (a+b+c)
# multi(1,2,3)


def decorator(even_no):
    def inner(p,q,r):
        p=p-1
        even_no(p,q,r)
    return inner
@decorator
def even_no(start,stop,step):
    for i in range(start,stop+1,step):
        print(i)
start=int(input("Enter starting value: "))
stop=int(input("Enter ending value: "))
step=int(input("Enter steps value: "))
even_no(start,stop,step)


   


