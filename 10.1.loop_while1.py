usr_age=input('enter your age')
age=int(usr_age)
usr_yr=input('enter the current year')
yr=int(usr_yr)

while age>=1:                                       #while check the condition given and proveed only if true
    print("you are", age, "years old in", yr)
    age=age-1
    yr=yr-1                                         #after this last line of while block code, the execution again go to line 6 for re-execution

if age==0:
    print('you are born in year', yr)

print('done')
