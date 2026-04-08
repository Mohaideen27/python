n=input("enter str ")
i=0
rev=''
while i<len(n):
    rev=n[i]+rev
    i+=1
print(rev)

if rev==n:
    print("PALINDROM")
else:
    print("NOT PALINDROM")