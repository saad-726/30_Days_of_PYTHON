#creating a set and including duplicate values and printing
my_set={1,2,3,4,5,2}
print(my_set)
#add and remove numbers
my_set.add(6)
my_set.remove(5)
print("Updated set :",my_set)
#union, intersection and difference
set1={1,2,3}
set2={5,4,3}
print("Union :",set1.union(set2))
print("Intersection :",set1.intersection(set2))
print("Difference :",set1.difference(set2))