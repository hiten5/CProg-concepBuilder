# total lines present in a file
f_name=input('enter the name of file')      
f_handle=open(f_name,'r')                   #open() function returns a file handle that is a way to access file, the open() function needs two parameters(both are string)
inp=f_handle.read()                         #one parameter is file name and another is mode, if mode is not mentioned then by default it is set to read ir 'r'=read and 'w'=write
count=0                                     #the read method create a continues series of string of all characters of file
for line in f_handle:                       #imp #here the for loop prints nothing because the f_handle is transferred to int and there is nothing left in file handle
    count=count+1
    print(line)                             #you notice this line prints all lines in file with two blank lines between them, reason is print by default have newline

print('total lines in file', count)         #also count=0 as there is no element in f_handle when for loop runs
print(inp)
print(len(inp))                             #the len function gives length of inp or number of characters in file
