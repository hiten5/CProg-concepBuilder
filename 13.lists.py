list_1=[2,4,5,8,10,12,14]
print(sum(list_1)/len(list_1))
list_1[2]=6
print(sum(list_1)/len(list_1))
list_1.append(16)
print(list_1)
list_1.append(0)
print(list_1)
print(range(len(list_1)))
#print(range(list_1))           range take int as parameter list_1 is list len(list_1) is integer, it returns opening and closing index +1 for list_1
#print(list_1.sort())
#print(list_1.max())
list_2=list()
while True:
    usrip=input('enter number to append, press d otherwise ')
    if usrip=='d':
        break
    else:
        list_2.append(int(usrip))    #append() function takes string as input so append('24') is correct but it append '24' as string to append as integer use int(number_string)

print(list_2)
print(list_1+list_2)

n=input('enter number to search, if not press n ')
print(list_1)
#print(n in list_1)                 #not work
if n=='n':
    n=0
else:
    print(int(n) in list_1)         #work

list_3=list_1+list_2
list_3.sort()                       #here sort() method modify the string and save it
#list_4=list_3.sort()               #not work as sort() method returns none
print(list_3)
print("maximum", max(list_3))
print("minimum", min(list_3))
print("sum", sum(list_3))
print("average", sum(list_3)/len(list_3))

var_1=input('enter the numbers with space ')
list_5=var_1.split()                #split() function split the string into parts, it cut it from parameter(by default set to space)
print(list_5)
