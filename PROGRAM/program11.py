a=list("vijay")
b=list("trisha")
for i in a:
    if i in b:
        b.remove(i)
        a.remove(i)
for i in 'flames':
    for j in range(len(b)+len(a)):
        
