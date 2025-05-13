#using default values in function parameters
def greet(name="guest"):
    print(f"Hello, {name}!")
greet("saad")
#sqaure or cube function
def nNum(num,power=2):
    return num**power
print(nNum(2))
print(nNum(2,3))
#keyword arguments
def display(name,age,salary):
    print(f"Name :{name} Age : {age} Salary :{salary}")
display(age=18,name="Saad",salary=12000)