usr_age=input('enter your age')

def eligiblity(a):
    while a>=0:
        if a<=5:
            print('you are eligible to get candy')
            break
        if a<=10:
            print('you are eligible to get coke')
            break
        if a<=15:
            print('you are eligible to get fruit beer')
            break
        if a<=20:
            print('you are eligible to get beer')
            break
        else:
            print('you are eligible to get anything')
            break

try:
    age=int(usr_age)
    eligiblity(age)
    print('thank and visit again')


except:
    print('thank and visit again')
