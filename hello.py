def my_function():
    print("hello")
my_function()

def get_greetings():
    return "hello there from funtion"
print(get_greetings())

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()
