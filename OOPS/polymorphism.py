# POLYMORPHISM -

# 1. COMPILE TIME -
# 2. RUN TIME -  I. Operator polymorphism 
            #     II. Function polymorphism 
            #    III. Method polymorphism 
            #     IV. Inheritence polymorphism 
            #      V. Method overriding polymorphism 

# I. OPERATOR POLYMORPHISM -
# x=10
# y=20
# z=10+20
# print(z)

# p='10'
# q='20'
# r=p+q
# print(r)


# II. IN-BUILT FUNCTION POLYMORPHISM -
# x='python'
# print(len(x))
# y=['python']
# print(len(y))


# III. USER-DEFINE FUNCTION POLYMORPHISM -
# def add(x,y):
#     return (x+y)
# print(add(10,20))
# print(add('10','20'))


# IV. METHOD POLYMORPHISM -
# class Student:
#     def detail(self):
#         print("I am student...")
# class Employee:
#     def detail(self):
#         print("I am employee...")
# Student().detail()
# Employee().detail()


# V. INHERITENCE POLYMORPHISM -
# class A:
#     def detail(self):
#         return None
# class B(A):
#     def detail(self):
#         return "Detail from B class..."
# class C(A):
#     def detail(Self):
#         return "Detail from C class..."
# obj1=B()
# print(obj1.detail())
# obj2=C()
# print(obj2.detail())




