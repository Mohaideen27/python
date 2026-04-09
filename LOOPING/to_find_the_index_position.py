l=[1,2,3,'d','g','d','e',[1,2],34]
print(l)
target=eval(input('Enter the value:  '))
for i in range(len(l)):
    if l[i]==target:
        print(i)
        break
else:
    print("element not found")