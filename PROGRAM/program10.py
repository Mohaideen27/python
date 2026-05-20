# WAPPT FIND THE FREQUENCY OF CHARACTER IN STRING USING YEILD
def out(n):
    for i in n:
        yield i,n.count(i)
print(dict(out("naveen")))