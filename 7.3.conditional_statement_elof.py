usr_ip=input('enter any number under 50')
try:
    usr=int(usr_ip)
except:
    print('please enter a number')
    
try:
    if usr<10:
        print('number is lower then 10')
    elif usr<20:
        print('number is between 10 and 20')
    elif usr<30:
        print('number is between 20 and 30')
    elif usr<40:
        print('number is between 30 and 40')
    elif usr<50:
        print('number is between 40 and 50')
    else:
        print('please enter number below 50')
except:
    print('thank you')