largest_so_far=-1
print('before', largest_so_far)
for the_num in [9,5,14,52,45,85,77,86,92,35,887]:       #for loop take variables in list one by one in iteration variable
    if the_num > largest_so_far:                        #iteration variable is the_num
        largest_so_far=the_num
    print(largest_so_far, the_num)

print('after', largest_so_far)
