# OOPS -
# ( class,object,constructor,self )

# (Day1)-

# Class -
# class_name should be starts with capital latter. 

# class Student:
#     '''hello...'''
#     school='SHSS'
#     def show():
#         print("welcome to the school")
# # print(dir(Student))
# print(Student.__doc__)


# class Student:
#     pass
# print(id(Student))
# obj1=Student
# print(id(obj1))
# obj2=Student
# print(id(obj2))


# Day2 -

# Constructor - Student()

# class Student:
#     pass
# obj=Student()
# obj1=Student()
# obj2=Student()
# print(id(Student))
# print(id(obj),id(obj1),id(obj2))


# class Student:
#     def __init__(self):
#         print("Constructor Called...")
#         print(id(self))
# # obj=Student 
# obj=Student() 
# print(id(obj))

# self holds the adḍress of the current object.
# class Student:
#     def __init__(self,name,quali):
#         self.n=name
#         self.q=quali
# obj1=Student('Himanshu','B.Tech')
# obj2=Student('Himanshu','B.Tech')
# print(id(obj1))
# print(id(obj2))
# print(obj1.n)
# print(obj2.n)


