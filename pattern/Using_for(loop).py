# Pattern (using for loop) -


# *
# **
# ***
# ****
# *****

# n=5
# for i in range(1,n+1):
#     print('*'*i)


#     *
#    **
#   ***
#  ****
# *****

# n=5
# for i in range(1,n+1):
#     print(' '*(n-i)  + '*'*i)

#     * 
#    * *
#   * * *
#  * * * *
# * * * * *

# n=5
# for i in range(1,n+1):
#     print(' '*(n-i)  + '* '*i)


# *****
# ****
# ***
# **
# *
    
# n=5
# for i in range(0,n):
#     print('*'*(n-i) + ' '*i )


# *****
#  ****
#   ***
#    **
#     *
    
# n=5
# for i in range(0,n):
#     print(' '*i + '*'*(n-i) )


# * * * * * 
#  * * * *
#   * * *
#    * *
#     *

# n=5
# for i in range(0,n):
#     print(' '*i + '* '*(n-i) )



#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * *
#   * * *
#    * *
#     *

# n=5
# for i in range(1,n+1):
#         print(' '*(n-i)  + '* '*i)
# for j in range(1,n):
#         print( ' '*j + '* '*(n-j) )



# * * * * * 
#  * * * *
#   * * *
#    * *
#     *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n=5
# for j in range(0,n):
#     print( ' '*j + '* '*(n-j) )
# for i in range(1,n+1):
#     print(' '*(n-i)  + '* '*i )