#print number from 1 to 10
for x in range (1,11):
    print(x)
#sum of numbers from 0 to 100
x=1
sum=0
while x<=100:
    sum=sum+x
    x+=1
print(sum)
#looping through a string and skipping letter O
string="python"
for char in string:
    if char=="o":
        continue
    else:
        print(char)