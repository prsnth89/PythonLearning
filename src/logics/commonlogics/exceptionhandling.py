try:
    1 / 0
except Exception as e:
    print("Exception occured--",e)
finally:
    print("Finally block")
