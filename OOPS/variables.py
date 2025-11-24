# Variables -  

# 1. INSTANCE VARIABLE - (Object dependent variable)
# self k sath jo variable apni value change krta h use instance varible h. (like. self.n/self.r)
# Object dependent variable is called instance variable. 

# class Student:
#     def __init__(self,name,roll_no):
#         self.n=name
#         self.r=roll_no
# obj1=Student('Himanshu',101)
# obj2=Student('Himanshu',102)
# print(obj1.n)
# print(obj1.r)
# print(obj2.n)
# print(obj2.r)


# Decleration of instance variable -
# 1. Inside Class ( using self) -   I. inside constructor
#                                  II. inside instance method 

# 2. Outside Class (using obj) -


# Example -
# class Student:
#     def __init__(self,name,roll_no):
#         self.n, self.r = name, roll_no            #decleration (inside constructor)
#     def addnow(self,contact):
#         self.c=contact                            #decleration (inside instance method)
# obj=Student('Neeraj',101)
# x=eval(input("Enter contact detail: "))
# obj.addnow(x)
# obj.city='Bhopal'                                 #decleration (Outside Class)         


# 1. Calling instance variable inside class -
# class Student:
#     def __init__(self,name,roll_no):
#         self.n, self.r = name, roll_no            
#         print(self.n,self.r)                      #calling(inside class)
#     def addnow(self,contact):
#         self.c=contact                            
# obj=Student('Neeraj',101)
 

#2. Calling instance variable inside instance method -
# class Student:
#     def __init__(self,name,roll_no):
#         self.n, self.r = name, roll_no            
#         print(self.n, self.r)                     #calling (inside instance method)
#     def addnow(self,contact):
#         self.c=contact                            
#         print(self.n, self.r, self.c, self.city)  #calling (inside instance method)
# obj=Student('Neeraj',101)

# x=eval(input("Enter contact detail: "))
# obj.city='Bhopal'                                 #decleration
# obj.addnow(x)
# print(obj.n, obj.r, obj.c, obj.city)              #calling (outside class)



# 2. CLASS VARIABLE - (object independent variable)
# obj change hone pe bhi value change ni krte.

# Example- 
# class Student:
#     school_name='SHSS'                            #decleration
#     def __init__(self,name,roll_no):
#         self.n, self.r = name, roll_no
#         Student.gread = '10th'                    #decleration
#     def addnew(self):
#         Student.principal='python'                #decleration
# Student.school_city = 'Bhopal'                    #decleration
# obj = Student('Neeraj', 101)
# obj.addnew()


# class Student:
#     school_name='SHSS'                                                  
#     def __init__(self,name,roll_no):
#         self.n, self.r = name, roll_no
#         Student.gread = '10th'                                         
#         print(Student.school_name, Student.school_city)                  #calling (class variable)
#     def addnew(self):
#         Student.principal='python'                                      
#         print(Student.school_city, Student.gread, Student.principal)     #calling (class variable)
# Student.school_city = 'Bhopal'                                          
# obj = Student('Neeraj', 101)
# obj.addnew()
# print(obj.principal)                                                     #calling (class variable-not recomended)
# print(Student.principal)                                                 #calling (class variable-recomended)



# 3. Local Variable - 

# class Student:
#     def __init__(self):
#         x=10
#         print(x)
#     def new(self):
#         y=20
#         print(y)
#         print(x)
# obj=Student()
# obj.new()

# Revision-

# class Student:
#     school='SHSS'
#     grade='10th'
#     def __init__(self,name,roll):
#         self.n, self.r = name, roll
#     @classmethod
#     def upgrade_grd(cls,new_gread):
#         cls.gread = new_gread
# obj1=Student('Neeraj',101)
# obj2=Student('Neeraj',102)
# obj1.upgrade_grd('11th') 
# # print(id(Student)) 
# print(obj1.grade)


# class Student:
#     grade='10th'
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll
#         if Student.grade:
#             self.g=Student.grade
#     def upgrade_grd(cls,new_grade):
#         cls.grade=new_grade
# obj=Student('neeraj',101)
# obj1=Student('himanshu',102)