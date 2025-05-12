def greet(my_list):
    for names in my_list:
        print(f"Hello, {names}!")
greet(["Saad","Shahmir","Zeeshan"])
#calculate function with parameter (a,b,operator)
def calc(a,b,op):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b
    else:
        print("Invalid Input")
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
operator=input("Enter the operator e.g(+, -, *, /)")
result=calc(num1,num2,operator)
print(f"The result of {num1} {operator} {num2} is : {result}")
#inner outer functions
def outer():
    def inner():
        print("Inner function executed!")
    inner()
outer()