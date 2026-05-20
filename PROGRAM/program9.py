def out(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i**2
        else:
            yield i**3
print(list(out(10)))