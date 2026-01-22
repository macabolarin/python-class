a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is less than a")

x = "hello"
y = 15
print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "banana", "orange"])

def myfunction() :
    return True
print(myfunction())
if myfunction():
    print("yes")
else:
    print("NO!")

animal = ["monkey", "cow", "rabbit"]
print("rabbit" in animal)

thislist = ["monkey", "cow", "goat"]
print(len(thislist))

thislistt = ["goat", "cow", "monkey"]
if "goat" in thislist:
    print("yes, 'goat' is in the list")

thislist = ["goat", "monkey", "cow"]
thislist.sort()
print(thislist)

thislist = ["10", "20", "30", "70", "23"]
thislist.sort()
print(thislist)