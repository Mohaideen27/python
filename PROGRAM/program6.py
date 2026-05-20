# def out():
#     for i in range(65,91):
#         yield chr(i),i
# print(dict(out()))

def out():
    for i in range(ord('A'),ord('Z')+1):
        yield chr(i),i
print(dict(out()))