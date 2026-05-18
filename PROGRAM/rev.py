n=int(input("Enter the number"))
s=1
if n<1:
    s=-1
    n=abs(n)
rev=0
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev*s)