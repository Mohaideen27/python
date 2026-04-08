# n=input("enter str ")
# i=0
# rev=''
# while i<len(n):
#     rev=n[i]+rev
#     i+=1
# print(rev)

n=input("Enter str: ")
i=len(n)-1
rev=''
while i>=0:
    rev=rev+n[i]
    i-=1
print(rev)