c=9
r=c//2+1
for i in range(r):
    for j in range(c):
        if i==r-1 or i+j==c//2 or j-i==c//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
n=9
for i in range(n):
    for j in range(3,n+3):
        if i ==j+3 or i <=j or i+j==n-1 or j==0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

