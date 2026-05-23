def kolar(func):
    def inner():
        print("Good Morning")
        func()
        print("Happy Pongal")
        print("Thank You")
    return inner()

name=["sameer", "naveen", "gopi"]
for i in name:
    @kolar
    def name():
        print (i)
    name()