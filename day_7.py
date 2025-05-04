#tuple of 5 elements and access third one
colors=("red","blue","green","pink","orange")
print(colors[2])
#unpacking a tuple
person = ("Saad", 22, "Karachi")
(name,age,city)=person
print(name)
print(age)
print(city)
#store 5 elements in tuple and print their sum and avg
tup=()
lis=[]
for x in range(5):
    num=int(input("Enter a number:"))
    lis.append(num)
tup=tuple(lis)
sum=0
for x in range(5):
    sum+=tup[x]
print("The sum is: ",sum)
print("The AVG is :", sum/5)