usr_age=input('enter your age')
age=int(usr_age)

while age>=0:                                       #break statement take the execution outside loop to line 20
    if age<=5:                                      #break statement can be used only in while and for loop
        print('you are eligible to get candy')      #without while in begining the break doesn't work
        break                                       #same is true for continue which reinitiate the execution of loop
    if age<=10:
        print('you are eligible to get coke')
        break
    if age<=15:
        print('you are eligible to get fruit beer')
        break
    if age<=20:
        print('you are eligible to get beer')
        break
    else:
        print('you are eligible to get anything')
        break

print('thank and visit again')
