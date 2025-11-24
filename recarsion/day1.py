# Recarsion -

# def fun_name(parameter):
#     #terminating point
#     if condition:
        #    | 
        #    | 
#     #recarsion call
#     fun_name(modified_paremeter)


# def natural_no(n):
#     if n==0:
#         return None
#     # print(n)               #  O\P 5,4,3,2,1
#     natural_no(n-1)
#     print(n)                 #  O\P 1,2,3,4,5

# x=int(input("enter number: "))
# natural_no(x)


# even-number -

# def natural_no(n):
#     if n==0:
#         return None
#     # print(n)               #  O\P 5,4,3,2,1
#     natural_no(n-1)
#     print(2*n)                 #  O\P 1,2,3,4,5 

# x=int(input("enter number: "))
# natural_no(x)

# odd-number -

# def natural_no(n):
#     if n==0:
#         return None
#     # print(n)               #  O\P 5,4,3,2,1
#     natural_no(n-1)
#     print(2*n-1)                 #  O\P 1,2,3,4,5 

# x=int(input("enter number: "))
# natural_no(x)

def natural_no(n):
    if n==0:
        return None
    # print(n)               #  O\P 5,4,3,2,1
    natural_no(n-1)
    sum=0
    sum=sum+2*n
    print(sum)                 #  O\P 1,2,3,4,5


x=int(input("enter number: "))
natural_no(x)




