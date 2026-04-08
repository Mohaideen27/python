n=int(input("Enter"))
count=0
prime=2
while count<=n:
    rem_count=2
    for i in range(2,prime):
        if prime%i==0:
            rem_count+=1
            break
        if rem_count==2:
            count+=1
            if count ==n:
                print(prime)
                break
        prime+=1
