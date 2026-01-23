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

x = 300

def myfunc():
    x = 200
    print(x)
myfunc()
print(x)

def myfunc():
    global x
    x = 300
myfunc()
print(x)

x = range(10)

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)

print("enter your name:")
name = input()
print(f'hello{name}')

name = input("enter your name:")
print(f"hello{name}")
fav1 = input("what is your favorite animal:")
fav2 = input("what is your favorite colour:")
fav3 = input("what is your favorite number:")
print(f"do you want a {fav2} {fav1} with {fav3} legs?")
