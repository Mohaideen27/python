n=eval(input("enter tuple"))
l=[]
i=0
while i <len(n):
    if type(n[i])==str:
        l.append(n[i])
    i+=1
print(l)