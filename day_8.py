Student={
    "Name" : "Saad",
    "Age": 17,
    "Grade": "A"

}

print ("Name is :", Student.get("Name"))
print ("Grade is :", Student.get("Grade"))
#add email and remove grade
Student.popitem()
Student.update({"email":"saad@test.com"})
print(Student)
#use loop to print dictionary items
product_prices = {
    "Apple": 2.5,
    "Milk": 1.8,
    "Bread": 2.0
}
for key,value in product_prices.items():
    print(key,value)