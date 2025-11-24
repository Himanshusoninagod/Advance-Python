# Methods-
#  1. Instance Method (first parameter in self)
#  2. Class Method (first parameter in cls) , @classmethod
#  3. Static Method (do not use either self or class as a first parameter) , @staticmethod
#     (with the use of static method we block self) 


# Class Method -

# class Book:
#     price=100
#     def __init__(self, title, total_page):
#         self.t=title
#         self.tp=total_page
#     @classmethod
#     def update_price(cls, p):
#         cls.price=p
# obj=Book('python', 500)
# print(obj.t, obj.tp, Book.price)
# # o/p - python 500 100
# x=float(input("Enter updated price: "))
# obj.update_price(110)

# obj1=Book('python', 510)
# print(obj1.t, obj1.tp, Book.price)
# # o/p - python 510 110


# Static Method -

# Example - (Error case) 
# class Web:
#     def __init__(self, name):
#         self.n=name
#     def gread():
#         print("Welcome to my web page")

# # obj = Web
# # obj.gread()

# obj = Web('ecom')
# obj.gread()


# Example - ( @staticmethod ) 
# class Web:
#     def __init__(self, name):
#         self.n=name
#     @staticmethod
#     def gread():
#         print("Welcome to my web page")
        
# # obj = Web
# # obj.gread()
# obj = Web('ecom')
# obj.gread()



