l=[10,0,1,0,-2,0,0,6]
l1=l.count(0)
l2=[]
for i in l:
    if i==0:
        continue
    l2.append(i)
l2.extend([0]*l1)
print(l2)