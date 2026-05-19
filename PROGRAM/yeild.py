def od(n):
    if n%2==0:
        print("Even")
        yield True
    else:
        print("Odd")
        return False
print(list(od(11)))
    