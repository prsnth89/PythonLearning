#simple if, else

light_is_on=False
if light_is_on:
    print("Light is on")
else:
    print("Light is off")

#elif [else if else if ]

name="test"
if name.lower()=="prasanth":
    print(f"Your name is --{name}")
elif name.lower()=="vimal":
    print(f"Your name is ---{name}")
else :
    print("Your name is not in given list")


#oneline if statement
a=10
b=20
c=15
print(f"a {a} is greater than b {b}") if a>b else print(f"a {a} is lower than b {b}")

#condition and or
if c==15 and a==10 :
    print(f"Value of C {c}")
elif c==15 or a==12:
    print(f"Value of A is 12")
else:
    print("Conditions didnt match")

a=2
#nested if

if a<5:
    print("A is lesser than 5")
    if a>1:
        print("A is greater than 1")
    elif a>15 and a<2:
        print("A is greater than 15")

