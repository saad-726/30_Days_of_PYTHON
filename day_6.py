#adding items in list
movies=["RRR","KGF","PK","Red Notice","13 Hours"]
movies.append("MI")
print(movies)
#adding/removing in list
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
numbers.insert(2,25)
print(numbers)
#input 5 numbers and add them in list print largest number and list in reverse order
num_list=[]
for x in range (5):
    num=input(f"Enter {x+1} number :")
    num_list.append(num)
print(list(reversed(num_list)))
print(max(num_list))