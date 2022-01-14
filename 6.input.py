a=input('what is your name')    #input() function is used to take data from user and it can also print string within it to tell user certain info
print('welcome', a)             #the user input is stored in memory block a, also here comma converts to space in output

b=input('enter number')         #the input() function stores input data as a string
#print(5+b)                     #generate error as b is a string even if we pass integer value to it
print(5+int(b))                 #give result only if user input is a number