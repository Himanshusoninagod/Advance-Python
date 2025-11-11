# File handling - 

# Syntex-
# open('file-name with extention', mode ) 

# Mode -
# 1. create
# 2. write
# 3. read
# 4. append



# f = open('1.py','r')
# data = f.read()
# print(data)
# f.close()

# f = open('1.py','r')
# data = f.read(10)
# print(data)
# f.close()

# f = open('1.py','r')
# data = f.readline()
# print(data)
# f.close()

# f = open('1.py','r')
# data = f.readlines()
# print(data)
# f.close()

# f = open('1.py','r')
# print(f.tell())
# f.close()

# f = open('1.py','r')
# print(f.tell())
# data = f.read()
# print(data)
# f.close()

# f = open('1.py','a')
# print(f.tell())
# data = f.read()
# print(data)
# f.close()

# f = open('1.py','r')
# data = f.readline()
# print(data)
# f.close()

# f=open('1.py','x')
# print(f.tell())

# do not open in write mode -
# f = open('1.py','w')
# data = f.read()
# print(data)



# f = open('1.py','r')
# print(f.tell())
# data = f.read(5)
# print(data)
# print(f.tell())

# data = f.read(10)
# print(data)
# print(f.tell())

# Cursor movement -
# syntex - seek(no. of bit move, from where(0,1,2))
# 0 - from starting
# 1 - from currentb position (only in binary mode'rb')
# 2 - from last position (only in binary mode'rb')


# f = open('1.py','rb')
# print(f.tell())
# f.seek(5)
# print(f.tell())
# f.seek(-5,1)
# print(f.tell())


# f = open('1.py','r') 
# print(f.tell())
# data = f.read()
# print(data)
# f.close()