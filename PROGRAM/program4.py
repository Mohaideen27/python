var=list(filter(lambda n:type(n)==int,[4,'hai',7,True,[1,2],8.9,(4,5),2,5,10]))
print(list(map(lambda n:n**2 if n%2==0 else n**3,var)))