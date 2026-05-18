a='hai hello how are you'
# print([i[0]+i[-1] for i in a.split()])
print(list(map(lambda a:a[0]+a[-1],a.split())))