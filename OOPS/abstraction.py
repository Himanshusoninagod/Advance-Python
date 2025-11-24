# ABSTRACTION - ( used for data protection)

# 1. inherit ABC (abstract based class) class 
# 2. at least one abstract method 
# 3. concrete method 

# Example-

from abc import ABC, abstractmethod
class Webpage(ABC):
    def dashboard(self):
        print("Welcome to dashboard...")
    def userprofile(self):
        print("Welcome to profile page...")
    @abstractmethod
    def login(self,user,password):
        pass
    @abstractmethod
    def signup(self,name,number):
        pass
class User(Webpage):
    def login(self,user,password):
        print("login successfully...")
    def signup(self,name,number):
        pass
obj=User()
obj.login("Himanshu",123)
obj.dashboard()
obj.userprofile()

# # x=input("enter username: ")
# # y=input("enter password: ")
# # obj.login(x,y)


