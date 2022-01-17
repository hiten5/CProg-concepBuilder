count=dict()
text=input('enter the text to analyse ')
words=text.split()

print('words: ', words)
print('counting......')

for string in words:
    count[string]=count.get(string,0) +1    #get() method search for key provided in parameter if found return its value but if not found then create one with default value 0

print('counts ', count)
for key in count:
    print(key, count[key])

print(count.keys())             #keys() method return all keys in dictionary
print(count.values())           #values() method return all values in dictionary
print(count.items())            #items() method return both key and value pairs
