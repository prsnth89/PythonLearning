def add_numbers(no1, no2):
    try:
        print(no1 + no2)
    except Exception:
        print("Please add only numbers")

import random
add_numbers(1, "Prasanth")
add_numbers(1, 3)


def add_two_numbers(no1, no2):
    if type(no1) != int or type(no2) != int:
        raise Exception('Inputs must be integer')
    print(no1 + no2)


add_two_numbers(3, 5)

try:
    add_two_numbers(3,
                    44.22)  # Throw error since type is not integer , if its outside try catch block then next line
    # 23 rd line wont get executed
except Exception as e:
    print(f'Exception occurred, please check the exception message--{e}')
add_two_numbers(3, 7)
