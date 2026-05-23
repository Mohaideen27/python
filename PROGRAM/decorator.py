def name(func):
    def inner(*arg,**kwargs):
        print("pretask")
        func(*arg,**kwargs)
        print("post task")
    return inner

@name
def middle():
    print("middle")
middle()

@name
def mid():
    print("mid")
mid()