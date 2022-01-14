x=1         #this would create a memory block named x in main memory and save constant 1 in it

y=2         #this would create a memory block named y in main memory and save constant 2 in it

z=x+y       #this would create a memory block named z in main memory and save value of expression x+y in it

a=x-y       #this would create a memory block named a in main memory and save value of expression x-y in it

b=x*y       # multiplication

c=x/y       # division

d=x**y      # raised to the power of ie x raise to the power y

e=x%y       #remainder or modulo operator ie remainder after dividing x by y

print(x)    #call function print passing parameter to it, here it is x. print function is used for displaying output on screen

print(y)

print(z)

print(a)

print(b)

print(c)

print(d)

print(e)

f=x*z

print(f)

g=1+2**3/4*5    #order of evaluation
                #some operators are more powerful and must be performed before others called operator precedence
                #parenthesis
                #power
                #multiplication, division and modulo
                #addition and subtraction
                #left to right in case of no operator precedence

print(g)        #the power is calculated first ie 2**3, then division happens as it comes before multiplication(left to right) and at last addition happens