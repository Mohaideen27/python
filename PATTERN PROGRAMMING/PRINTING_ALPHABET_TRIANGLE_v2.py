n=int(input("enter any odd no."))
c=90
for i in range (n):
    #c=90
    for j in range(n):
        if i<=j:
            print(chr(c),end=" ")
        else:
            print(" ",end=" ")
    c-=1
    print()