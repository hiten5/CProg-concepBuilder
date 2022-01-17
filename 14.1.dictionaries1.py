purse=dict()                #dictionary is created and saved with variable name purse
purse['money']=12           #this is way to append items to dictionary, item have key and value pair
purse['candy']=3            #the candy is key and 3 is its value
print(purse)                #in dictionary there is no indexing and values are called by their key
print(purse['money'])

usr_1=input('enter the number of things you keep in your purse')
a=0

while a<int(usr_1):
    a=a+1
    usr_2=input('name item ')
    if usr_2 in purse:
        usr_3=input('how many ')
        purse[usr_2]=purse[usr_2]+int(usr_3)
    else:
        purse[usr_2]=0                                  #get() method take two parameters key and default value, it search for key in dictionary
        usr_3=input('how many ')                        #and if key is not found it automatically creates one with provided key name and assign default value to it
        purse[usr_2]=purse[usr_2]+int(usr_3)            #if key is found then it returns its value

print('items in your purse ', purse)
