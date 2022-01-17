fnam=input('enter the file name ')
f_han=open(fnam)

#f = something
#try:
    # do stuff with f
#finally:    # even if an exception occurs
    # close f (call its __exit__ method)
# now you can no longer use f

count=0
sea=input('enter the string to search ')

for line in f_han:
    if sea in line:
        count=count+1
f_han.close()

print('keyword found in file', count, 'times')
usrip=input('enter y to see results ')

def finder(sea):
    f_han=open(fnam)
    for line in f_han:
        if sea in line:    
            print(line.rstrip())
    f_han.close()

if usrip=='y':
    finder(sea)
else:
    print('thanks')
