
# n=9
# for i in range(n):
#     for j in range(n*2):
#         if j==0 or j==n-1:
#             print('||',end=" ")
#         elif i==j:
#             print(r"\\" ,end=" ")
#         elif i==j:
#             print(r"\\" ,end=" ")
#         else:
#             print(end='   ')
#     print()
n=5
for i in range(n):
    for j in range(n*2):
        if j==0 or j==n-1:
            print('||',end="    ")
        elif i==j:
            print(r"\\" ,end="    ")
        elif i+n-1==j:
            print(r"\\" ,end="    ")
        elif j==n*2-1:
            print('||' ,end="    ")
        else:
            # print(end='   ')
            print(end="      ")
    print() 
# n=9
# for i in range(n):
#     for j in range(n):
#         print(i,j, end='   ')
#     print()