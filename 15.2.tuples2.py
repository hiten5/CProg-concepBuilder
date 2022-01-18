# top 10 most frequent words in file
fnam=input('enter the file name')
handle=open(fnam)
count=dict()
list_1=list()

for line in handle:
    sp=line.split()
    for word in sp:
        count[word]=count.get(word, 0)+1

for k,v in count.items():
    list_1.append((v,k))

list_2=sorted(list_1, reverse=True)
print(list_2[:10])
