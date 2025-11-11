# Pattern (using while loop) -

# *****
# *****
# *****
# *****
# *****

# n=5
# i=1
# while i<=n:
#     print('*'*n)
#     i=i+1


# *
# **
# ***
# ****
# *****

# n=5
# i=1
# while i<=n:
#     print('*'*i + ' '*(n-i))
#     i=i+1

#     *
#    **
#   ***
#  ****
# *****

# n=5
# i=1
# while i<=n:
#     print(' '*(n-i)  + '*'*i)
#     i=i+1


#     *
#    * *
#   * * * 
#  * * * *  
# * * * * *

# n=5
# i=1
# while i<=n:
#     print(' '*(n-i)  + '* '*i)
#     i=i+1


# *****
# ****
# ***
# **
# *
 
# n=5
# i=0
# while i<n:
#     print('*'*(n-i) + ' '*i)
#     i=i+1 


# *****
#  ****
#   ***
#    **
#     *

# n=5
# i=0
# while i<n:
#     print(' '*i + '*'*(n-i))
#     i=i+1 

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n=5
# i=0
# while i<n:
#     print( ' '*i + '* '*(n-i) )
#     i=i+1




# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# n=5
# i=1

# while i<=n:
#     print('*'*i + ' '*(n-i))
#     i=i+1
# i=i-2

# while i>=1:
#     print('*'*i + ' '*(n-i))
#     i=i-1



#     *
#    **
#   ***
#  **** 
# *****
#  ****
#   ***
#    **
#     * 


# n=5
# i=1

# while i<=n:
#     print(' '*(n-i) + '*'*i)
#     i=i+1
# i=i-2

# while i>=1:
#     print(' '*(n-i) + '*'*i)
#     i=i-1


# n=5
# i=1

# while i<=n:
#     print(' '*(n-i) + '* '*i)
#     i=i+1
# i=i-2

# while i>=1:
#     print(' '*(n-i) + '* '*i)
#     i=i-1



# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n=5
# i=0
# while i<n:
#     print(' '*i + '* '*(n-i))
#     i=i+1
# i=i-2
# while i>=0:
#     print(' '*i + '* '*(n-i))
#     i=i-1

# *****
#  ****
#   ***
#    ** 
#     *
#    **
#   ***
#  ****
# *****

# n=5
# i=0
# while i<n:
#     print(' '*i + '*'*(n-i))
#     i=i+1
# i=i-2
# while i>=0:
#     print(' '*i + '*'*(n-i))
#     i=i-1


# ch='A'
# char----ASCII (ord())
# ASCII----char (chr())


# A B C D E 

# ch='A'
# n=int(input("Enter how many charecters you want to print :"))
# i=1
# while i<=n:
#     print(ch, end=' ')
#     ch=chr(ord(ch)+1)
#     i=i+1


# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

# ch='A'
# n=int(input("Enter how many charecters you want to print :"))
# i=1
# for i in range(n):
#     ch='A'
#     for j in range(n):
#         print(ch, end=' ')
#         ch=chr(ord(ch)+1)
#     print()

# or

# n=int(input("Enter how many charecters you want to print :"))
# i=1
# while i<=n:
#     ch='A'
#     j=1
#     while j<=n:
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#         j=j+1
#     print()
#     i=i+1




# A 
# A B
# A B C
# A B C D
# A B C D E

# n=int(input("Enter how many charecters you want to print :"))
# i=1
# while i<=n:
#     ch='A'
#     j=1
#     while j<=i:
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#         j=j+1
#     print()
#     i=i+1


# A 
# B C
# D E F
# G H I J
# K L M N O

# n=int(input("Enter how many charecters you want to print :"))
# i=1
# ch='A'
# while i<=n:
#     j=1
#     while j<=i:
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#         j=j+1
#     print()
#     i=i+1


# A 
# C E
# G I K
# M O Q S
# U W Y [ ]

# n=int(input("Enter how many charecters you want to print :"))
# i=1
# ch='A'
# while i<=n:
#     j=1
#     while j<=i:
#         print(ch,end=' ')
#         ch=chr(ord(ch)+2)
#         j=j+1
#     print()
#     i=i+1

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n=int(input("Enter number: "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end=' ')
#         j=j+1
#     print()
#     i=i+1

# 2 
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10

# n=int(input("Enter number: "))
# i=1
# while i<=n:
#     j=1
#     a=2
#     while j<=i:
#         print(a,end=' ')
#         a=a+2
#         j=j+1
#     print()
#     i=i+1



# 1 
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9

# n=int(input("Enter number: "))
# i=1
# while i<=n:
#     j=1
#     a=1
#     while j<=i:
#         print(a,end=' ')
#         a=a+2
#         j=j+1
#     print()
#     i=i+1