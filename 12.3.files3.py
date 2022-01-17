# get all lines in a file that have "@uct.ac.za" as substring
fnam=input('enter the name of file')
fhand=open(fnam)
for line in fhand:
    line=line.rstrip()
    if '@uct.ac.za' not in line:        #if line does not have string in it then loop reinitiated
        continue                        #this thelp in better memory optimization as most files not have string in them
    print(line)                      
