
if 2>1 :
    print ("2 is greater than 1")
    if 2>1:
        print("2 is greater than 1")
    # statement is not allowed if its in same line

x=4
y="Prasanth"
print(x)
print(y)

z=5  #variables can be changed without defining type
z="Test five"
print("---variables can be changed without defining type---")
print(z)

#casting
a=str(3)
b=int(3)
c=float(3)
print("---casting---")
print("Type of variable a is ",type(a),"--value is--"+a)
print("Type of variable b is ",type(b))
print("Type of variable c is ",type(c))

#Assigninig multiple values
d,e,f="Assign d",33.001,121332332121
print("---Assigninig multiple values---")
print(d)
print(e)
print(f)

print("Print multiple values---"+d,e,f)
#one value multiple variable
d=e=f="orange"
print("one value multiple variable")
print(d)
print(e)
print(f)

#unpack collections
fruits=["Apple","Banana","Cherry"]
print(fruits)
fruit1,fruit2,fruit3=fruits
print("unpack collections")
print("Fruit 1--"+fruit1)
print("Fruit 2--"+fruit2)
print("Fruit 3--"+fruit3)

#Function
def myFunction():
   global name
   name="Prasanth"  #scope is jus inside method , if you mention variable name as global then it can accessed anywhere
   print("My First python program and name is "+name)

myFunction()
print(name)


#Combination of and, not, or
x=True
y=True

print('x',x)
print('y',y)
print('Not x',not x)
print('Not y',not y)
print("Print x or y ",x or y)
print("Print x and y",x and y)