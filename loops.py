# #for loop
# for i in range(1, 1000): # loop from 1 to 999 we have to set the range
#     print(i)


# #while loop

# i=1
# while(i<51): # loop from 1 to 50 , while loop checks the condition and then executes the code,here the condition is i<51 .it will print until i condition is true and stop once it becomes false
#     print(i)
#     i+=1

# i=0
# while i < 6:
#     print("Mohammed")   this will print mohammed name 5 times  
#     i=i+1

# print a loop of lists in python

# l = ["mohd" , True , "rohan", "halla" , 54] # list of different data types
# i=0 
# while(i<len(l)): # loop will run until the condition is true ie i will run until it is less than the length of the list
#     print(l[i])
#     i+=1


for i in range(100):
    if(i==53):
        break
    print(i)


for i in range (5):
    if i==0 :
        continue #continue will skip the current iteration and move to the next one whereas break
    print(i**2)