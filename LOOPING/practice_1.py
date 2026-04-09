# WAPPT MOVE ALL THE ZEROS FROM LEFT SIDE TO THE LIST DATATYPE.

l=[10,0,1,0,-2,6,0]
for i in range(len(l)):
    if l[i]==0:
        val=l.pop(i)
        l.append(val)

print(l)