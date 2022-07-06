# simple function
def car():
    print("i have 4 cars")


car()

for number in range(10):
    car()


# function with parameters
def car(carname):
    print(carname)


car("My carname is BMW")


# function with return type
def car(carname):
    return carname


carName = car("Tesla")
print(f"Return type of function car is {carName}")

# assigning print function to a variable
print("Hello", "World", "Concatenate strings")
new_print = print
new_print("Test new print")


# return statement without specifying datatype
def add_no(num1, num2=6):  # num2=6 ,if the function didnt pass any value then it will take default value of 6
    result = num1 + num2
    result = result / 1.5
    return result


print("Added nos---", add_no(2))  # default value of 6 will be picked up
print("Added nos---", add_no(2, 12))


def multiple_Arguments(name, arg2=None, arg3=55, arg4=True):  # None
    pass  # functions cannot be empty, if you dont want to do anything jus give pass


def multiple_Arguments(name, arg2=None, arg3=55, arg4=True):  # None
    print("Name is --",name)
    print("Arg 2 is---",arg2)
    print("Arg 3 is ---",arg3)
    print("Arg 4 is---",arg4)

multiple_Arguments("Prasanth",arg4=False)
