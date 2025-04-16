#print a program to take input from user and create a multiplication table 

n= int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n * i}")
 