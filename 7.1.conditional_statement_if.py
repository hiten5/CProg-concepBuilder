print('program to find whether number is odd or even')
usr_ip=int(input('enter the number'))                   #the int() function will get the integer value from string entered by user
rem=usr_ip%2                                            #used to calculate remainder

if rem == 0:                                            #condition if true then proceed otherwise skips the if statement block
  print('number is even')                               #notice space in begining, space marks block- the block next to if statement
if rem == 1:
  print('number is odd')


#usr_ip=input('enter the number')
#rem=int(usr_ip)%2                                      #the int() function will get the integer value from string usr_ip