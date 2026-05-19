# WAPPT TO FIND THE SQUARE OF ALL THE VALUE BETWEEN 1 TO 10

# def sq(n):
#     for i in n:
#         yield i*i
# print(list(sq(range(1,11))))

def sq():
    out=[]
    for i in range(1,11):
        out.append(i*i)
    return out
print(sq())