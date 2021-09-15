def greet(name):
    print("hello,"+name+"!")
    greet2(name)
    print("getting ready to say goodbye……")
    bye()

def greet2(name):
    print("how are you,"+name+"?")
def bye():
    print("ok,bye!")

greet("Ryan")
