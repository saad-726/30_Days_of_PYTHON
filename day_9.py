# 1. Set and duplicate add
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.add(3)  # duplicate won't be added
print("Set after adding:", my_set)

# 2. Union, intersection, difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))

# 3. User input and remove smallest
user_set = set()
for x in range(5):
    num = int(input(f"Enter unique number {x+1}: "))
    user_set.add(num)

print("Set before removal:", user_set)
smallest = min(user_set)
user_set.remove(smallest)
print("Set after removing smallest number:", user_set)
