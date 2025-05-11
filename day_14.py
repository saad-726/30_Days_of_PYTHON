#creating a dictionary
my_dict={
    "Name":"Saad",
    "Age":19,
    "Country":"Pakistan"
}

print(my_dict["Name"])
print(my_dict["Age"])
print(my_dict["Country"])
#updating age value
my_dict.update({"Age":18})
print("Updated Dictionary",my_dict)
#using loop to iterate through dictionary

for key,values in my_dict.items():
    print(f"{key} :{values}")