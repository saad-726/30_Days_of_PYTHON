def greet(name):
    print(f"Hello {name}!")
greet("saad")
name=input("Enter your name :")
greet(name)
#add number and display result
def add(a,b):
    return a+b
def display(x):
    print("The result is:",x)
x=add(7,8)
display(x)
#pass list and return largest number
def large(list):
    print(max(list))
list=[1,2,3,4]
large(list)