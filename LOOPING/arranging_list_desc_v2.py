# [5,4,1,2,3,34]
l=eval(input("Enter List: "))
for i in range(len(l)-1):
    for j in range(i+0, len(l)):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
