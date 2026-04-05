c=int(input("enter any odd no."))
r=c//2+1
for i in range(r):
    for j in range(c):
        if i==r-1 or i+j==c//2 or j-i==c//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()