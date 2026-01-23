a = 33
b = 333
if b > a:
    print("b is greater than a")

    number = 15
    if number > 0:
        print("the number is positive")

age = 18
if age >= 18:
    print("ypu are eligible")
    print("you can vote")
    print("you are legally right")
    print("you are enfranchised")

is_logged_in = True
if is_logged_in:
    print("welcome back")

a = 33
b =33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade: c")
elif score >= 60:
    print("Grade: D")

age = 25

if age < 13:
    print("you are a child")
elif age < 20:
    print("you are a teenager")
elif age < 60:
    print("you are an adult")
elif age < 65:
    print("you are a senior")

number = 7
if number % 2 ==0:
    print("the number is even")
else:
    print("the number iis odd")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("both conditions are true")

username = "drake"
password = "const"
is_verified = True

if username and password and is_verified:
    print("login successful")
else:
    print("login failed")

username = "mich"
password = "mich123"
is_active = True

if username:
    if password:
        if is_active:
            print("login successful")
        else:
            print("account is not active")
    else:
        print("password required")
else:
    print("username required")

a = 33
b = 330
if b > a:
    pass

age = 16
if age < 18:
    pass
else:
    print("access granted")