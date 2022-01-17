# get all lines in a file that starts with "From"
f_name=input('enter the name of file')
f_handle=open(f_name,'r')
for line in f_handle:
    if line.startswith('From'):
        line=line.rstrip()          #to remove extra line that appear as print default of newline
        print(line)                 #remember line.strip() only don't work as it is method which just change the string but not save it
        
