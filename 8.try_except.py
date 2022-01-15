usr_ip=input('enter any number')        #takes input from user and save it as a string
try:                                    #this block is in try because user can enter a character string instead of number and that can blow our program
    usr=int(usr_ip)                     #if user input number then ok, code skip except section and proceed
except:                                 #if try section produces error as user input character then except section executes to save from program stallation due to error
    usr= -1

if usr >= 0:
    print('good job you know what a nuber is, hahaha :-)')
else :
    print('this is not a number')
