word=input("Enter a string :")
Uword=word.upper()
print(Uword.replace(' ','_'))
#counting words
def counter(string):
    data=string.split(' ')
    return len(data)
data=input("Enter a string :")
x=counter(data)
print(x)

email = input("Enter your email: ")
if email.endswith("@gmail.com") and len(email.split("@")[0]) >= 3:
    print("Valid Gmail address ✅")
else:
    print("Invalid Gmail address ❌")