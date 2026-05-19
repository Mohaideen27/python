# l=[12,34,5,3,'the',7+2j,True]
# check=lambda n:type(n)==int
# fil=filter(check,l)
# print(sum(list(fil)))


  
print(sum(list(filter(lambda n:type(n)==int,[12,34,5,3,'the',7+2j,True]))))