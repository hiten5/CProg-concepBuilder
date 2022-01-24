'''
Write a function delchar(s,c) that takes as input strings s and c, 
where c has length 1 (i.e., a single character), and returns the string obtained by deleting all 
occurrences of c in s. 
If c has length other than 1, the function should return s

Here are some examples to show how your function should work.

 
>>> delchar("banana","b")
'anana'

>>> delchar("banana","a")
'bnn'

>>> delchar("banana","n")
'baaa'

>>> delchar("banana","an")
'banana'
'''

def delchar(s,c):
    a = ""
    if len(c) == 1:
        for i in s:
            if i == c:
                pass
            else:
                a = a + i
        return(a)
    else:
        return(s)

print(delchar("banana","b"))
print(delchar("banana","a"))
print(delchar("banana","n"))
print(delchar("banana","an"))