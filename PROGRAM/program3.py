# WAPPT SHOW PRIME NO. BTWN 1 TO 20

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(list(filter(prime,range(2,21))))


# print([i for i in range(2,21)if i%i!=0])
        
