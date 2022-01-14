x='hello'   #the memory block x saves the string constant

y='world'

z=x+y       #the addition of two strings is called concatenation, so operator + performs concatenation in strings

print(z)    #the result would be a concatenated word ie helloworld

a='hello ' + 'world ' + 'i am hs'     #note the space included in first two words

print(a)

b=type(x)   #type() function is used to get the type of parameter passed to it

print(b)    #print() function will print the type of variable x

c=type(y)

print(c)

d=type(z)

print(d)

e=type(a)

print(e)

f=10

print(type(f))      #this is basically function within a function, here type function will fet type of f then print will print its type

print(type(25))

print(type(25.0))

print(type('hi'))
