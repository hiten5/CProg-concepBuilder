s= 'monty python'
p= 'comedy circus'
print(s)
print(s[0:4])           #the numbers inside, ie for [a:b], slice string from index a(including a) to b(excluding index b)
print(s[6:20])          # space is also indexed
print(s[7:])            #[a:] means from a to end
print(s[:7])            #[:b] means from start to b(excluding index b)
print(s+p)              #concatenation, note no space between s and p strings
print(s+' '+p)          #concatenation of space between two strings
a= 'monty' in s         #in see whether string monty is present in s or not
print(a)                #in is boolean returning keyword so a will have either true or false

if s>p:                             #strings can be compared also based on utf values
    print(s, 'comes after', p)
else:
    print(p, 'comes after', s)

b= 'AMITABH bacchan'
print(b.lower())                    #lower() is method which turns all characters of b to lowercase, upper() does opposite
print(b.upper())                    #the original string remains unchanged
print(b.capitalize())
dir(b)                              #dir(a) return all methods available for a

print(b.find(' '))                  #b.find(a) method return the position of passed parameter string a in b, if not found will return -1

f='iatsimba@gmail.com'
g=f.find('@')                       #find position of @ in f
h=f.find('.',g)                     #find position of . after position g
print(f[g:h])

c= b.replace('AMITABH','Abhishek')  #c.replace(a,b) look for every a in c and replace it with b
print(c)

d='     I am a foody person.      '
print(d.strip())                    #remove white spaces from begining and end
print(d.lstrip())                   #remove white spaces of left end
print(d.rstrip())                   #remove white spaces of right end

e= b.startswith('Amit')             #will find if string b starts with Amit, return true or false
print(e)                            #false as Amit and AMIT are different strings
