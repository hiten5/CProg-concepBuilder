# count frequency of user inputted text in file
fnam=input('enter the file name ')

try:
    f_han=open(fnam)
except:
    print('please enter correct file name')

count=0
for line in f_han:
    if 'program' in line:
        count=count+1

print('keyword found in file', count, 'times')
