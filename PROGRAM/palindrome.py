# def pal(n):
#     return n==n[::-1]

print(list(filter(lambda n:type(n)==str and n==n[::-1],['sam',47,45,'mom','mam'])))