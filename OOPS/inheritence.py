# 1. INHERITANCE - (PARENT-CHILD RELATION)

# Syntex-
# class Parent:
#     pass
# class Child(Parent):
#     pass

# Types of Inheritence -
# 1. Single-level (PARENT----CHILD)
# 2. Multi-level  (GRAND-PARENT----PARENT----CHILD)
# 3. Multiple     (FATHER----MOTHER)
#                         |   
#                        CHILD 
# 4. Hierarichical
# 5. Hybrid



# I. SINGLE LEVEL INHERITENCE -

# class Parent:
#     car='Nexon'
#     def home(self):
#         print("Home from parent")
# class Child(Parent):
#     pass
# obj=Child()
# print(obj.car)
# obj.home()


# class Parent:
#     car="Nexon"
#     def home(self):
#         print("home from parent")
# class Child(Parent):
#     def home(self):
#         print("home from child")
#         super().home()                    #super() --- to access same method of parent class and child
# obj=Child()
# obj.home() 



# II. MULTI-LEVEL INHERITENCE -

# class Grandparent:
#     car='bmw'
#     def home(self):
#         print("hello from Grandparent...")
# class Parent(Grandparent):
#     car='mersedies'
#     def home(self):
#         super().home()
#         print("hello from Parent...")
# class Child(Parent):
#     car='nexon'
#     def home(self):
#         super().home()
#         print("hello from Child...")
# obj=Child()
# obj.home()
# print(Child.car)
# print(Parent.car)
# print(Grandparent.car)


# III. MULTIPLE INHERITENCE -

# class A:
#     def home(self):
#         print("home from parent1...")
#         B.home(self)       # B().home()
#     def car(self):
#         print("car from parent1...")
# class B:
#     def home(self):
#         print("home from parent2...")
#     def bank(self):
#         print("bank from parent2...")
# class C(A,B):         # MRO (depth first algorithum)
#     def home(self):
#         super().home()
#         print("home from child...")
# obj=C()
# obj.home()
# obj.bank() 
# obj.car() 



# IV. HIERARICHICAL -

# class Parent:
#     car='nexon'
#     def home(self):
#         print("hello from parent...")
# class Child1(Parent):
#     car='TATA'
#     def home(self):
#         super().home()
#         print("hello from child 1...")
# class Child2(Parent):
#     car='BMW'
#     def home(self):
#         super().home()
#         print("hello from child 2...")

# obj=Child1()
# print(obj.car)
# obj.home()

# obj1=Child2()
# print(obj1.car)
# obj1.home()



# # V. HYBRID -

# class A:
#     def home(self):
#         print("home from A...")
# class B(A):
#     def home(self):
#         super().home()
#         print("home from B...")
# class C(A):
#     def home(self):
#         super().home()
#         print("home from C...")
# class D(B,C):
#     def home(self):
#         super().home()
#         print("home from D...")
# obj=D()
# obj.home()

