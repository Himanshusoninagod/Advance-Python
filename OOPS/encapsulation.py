# ENCAPSULATION -

# Access specifier/modifier -
    #     I. public/localvariable or method 
    #    II. protected variable or method 
    #   III. private variable or method 


# 1. public variable or method -
# class A:
#     x=10              #public variable
#     def show(self):
#         print("Hello...")
# class B(A):
#     pass
# obj=B()
# print(obj.x)        #through object
# obj.show()
# print(A.x)          #through class


# 2. protected veriable or method - (not supported in python)
# class A:
#     _x=10
#     def _show(self):
#         print("Hello...")
# class B(A):
#     pass
# obj=B()
# print(obj._x)        #through object
# obj._show()
# print(A._x)          #through class(accessable ooutside class)


# 3. private variable or method -
# name mangling (_ classname __ variable/method)

# class A:
#     __x=10              #public variable
#     def __show(self):
#         print("Hello...")
# class B(A):
#     pass
# obj=B()
# # print(obj.__x)        #through object(error)
# # obj.__show()
# # print(A.__x)          #through class(error)

# print(A._A__x)         #accessable thrugh - name mangling (_ classname __ variable/method)

# print(dir(A))       

# try:
#     print(obj.__x)
# except AttributeError:
#     print("hello")

