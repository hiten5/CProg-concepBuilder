def largest(a):
    max = a[0]
    for i in a:
        if int(i) > max:
            max = int(i)
    print( max )

b = [50,100,150,5,2000]

largest(b)