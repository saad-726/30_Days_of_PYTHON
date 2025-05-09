elem=("Saad",19,6.0)
for x in range (3):
    print(elem[x], type(elem[x]))
#converting tuple to list and adding an element then converting back to tuple
tup1=(1,2,3,4,5)
list1=list(tup1)
list1[4]=6
tup1=tuple(list1)
print(tup1)
#trying to change tuple value
emtuple=(1,2,3,4)
emtuple[2]=5
print(emtuple)