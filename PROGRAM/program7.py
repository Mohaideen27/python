def out(n):
    a=n.split()    
    for i in a:
        if len(i)%2==0:
            yield len(i),i.upper()
        else:
            yield i,i.upper()
b=out('i love vijay')
print(dict(b))








# py='i love trisha'
# l=py.split()
# for i in l:
#     if i%2==0:
#         l[i].count()
#     else:
#         l[i]