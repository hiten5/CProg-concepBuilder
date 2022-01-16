def greet(lang):            #function with name greet and argument lang is created, lang is not stored in main memory
    if lang=='es':          #the argument is compared
        return ('hola')     #return is the output of the function greet, after executing return the function terminates and its output is generated
    elif lang=='fr':
        return ('bonjour')
    else:
        return ('hello')

usr_ip=input('enter the language you speak options are es for spanish fr for french eng for english ')
print(greet(usr_ip), 'dear')
