'''
A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .

Write a Python function primeproduct(m) that takes an integer m as input and returns True 
if m is a prime product and False otherwise. (If m is not positive, your function should return False.)

Here are some examples of how your function should work.
>> primeproduct(6)
True

>>> primeproduct(188)
False

>>> primeproduct(202)
True
'''

def primeproduct(m):
    a = []
    b = True
    for i in range(2,m):
        if m%i == 0:
            a.append(i)
    print(a)
    for x in a:
        for y in range(2,x):
            if x%y==0:
                b = False
    if len(a) == 0:
        b = False
            
    return(b)
        

primeproduct(6)
primeproduct(188)
primeproduct(202)
primeproduct(21)
primeproduct(4)
primeproduct(2)