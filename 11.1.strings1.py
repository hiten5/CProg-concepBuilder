usr_ip=input('enter any string')
vow=0
def count(x):
    global vow              #vow is defined outside function count() so it is a global variable
    vow=vow+1               #counting for each time function is called
    print(x, 'is vowel')

for a in usr_ip:            #a temporarily save the each character of string for once in a loop
    if a=='a':              #a=h for usr_ip[0] in 1 loop
        count(a)            #a=i for usr_ip[1] in 2 loop
    elif a=='e':            #a=t for usr_ip[2] in 3 loop
        count(a)            #here the user input is hit
    elif a=='i':
        count(a)
    elif a=='o':
        count(a)
    elif a=='u':
        count(a)
    else:
        print(a)

print('the total number of vowels are', vow)
