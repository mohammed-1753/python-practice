e=int(input("enter your age: "))

if(e%2==0): #this is independent if statement and multiple if statements can be run in a single program
    print("the number entered is even ")
else:
    print("the number entered is odd")
if(e>=30): #if entered age id greater than or equal to 30
    print("you are adult and yes")
    print("you should be married by now")
elif(e==0): #if entered age is 0
    print("its invalid age you idiot😒")
else: #if entered age is less than 30
    print("you're below 30 kid😠")
print("shadi ka form laaavv")

#p2

marks1=int(input("enter your marks1:"))
marks2=int(input("enter your marks2:"))
marks3=int(input("enter your marks3:"))

total_percentage=(100*(marks1+marks2+marks3)/300) #total percentage is calculated by adding all the marks and dividing by 300
if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33): #if total percentage is greater than or equal to 40 and all the marks are greater than 33
    print("you're passed now fuck off",total_percentage)
else:
    print("you're failed now take of your pants",total_percentage)   

# p3     spam checker

p1="bhai"
p2="bhen"
p3="mummy"
p4="pappa"

message=input("enter your comment: ")
if(p1 in message or p2 in message or p3 in message or p4 in message): #if any of the words are present in
    print("its a spam and bad word") #if all the names are present in the message 
else:
    print("its not and all is well!..")

