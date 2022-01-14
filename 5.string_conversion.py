a='123'             #a is a string

print(type(a))

b=int(a)            #now a is passed to function int() and int() scans it and get integer value from a, as it is pure number string

print(b)

print(type(b))      #b is already defined as integer

c='hello21'         #c is mixed string
#d=int(c)           #this code gives error as partial numerical string can not be integer
#print(d)
#print(type(d))

e='21 hi'
#f=int(e)
#print(f)