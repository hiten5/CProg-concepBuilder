#list brackets []
#dictionary brakets {}
#tuples brakets ()
#tuples are immutable
#tuples are used for temporary variables to save space

d=dict()
d['ram']=1
d['laxman']=2
d['abhimanyu']=3

t=d.items()
sorted(t)                     #sorted function sort the tuples inside list t but doesnt change the original list
print(t)
print(sorted(t))

print(d)

for k,v in d.items():         #to revert the order of key and value pair
    print(v,k)

a=(0,1,2)<(5,1,2)             #tuple comparison, it compare the 1 entry then second if no conclusion is derived from 1
print(a)

#sort by values
c={'a':10, 'b':1, 'c':220}
tmp=list()

for k,v in c.items():
    tmp.append((v,k))

tmp.sort()                  #sort min to max
print(tmp)

tmp.sort(reverse=True)      #sort max to min
print(tmp)

tmp_2=sorted(tmp)           #sorted function returns sorted values of prameter and does not alter the original list
print(tmp_2)
print(tmp)
