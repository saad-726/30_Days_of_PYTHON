#eligible to vote or not
age=int(input("Enter your age :"))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible for voting")

#check positive,neagtive or zero
num=int(input("Enter a number :"))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("You entered zero")
#check for password python123
password=input("Enter your password :")
if password=="python123":
    print("Access granted")
else:
    print("Access denied")
    