# Q1 create a list of marks by taking input from users

marks = []
f1 = input("ENter mRKS name :")
marks.append(f1)
f2 = input("ENter mRKS name :")
marks.append(f2)
f3= input("ENter mRKS name :")
marks.append(f3)
f4 = input("ENter mRKS name :")
marks.append(f4)
f5 = input("ENter mRKS name :")
marks.append(f5)
f6 = input("ENter mRKS name :")
marks.append(f6)
f7= input("ENter mRKS name :")
marks.append(f7)
marks.sort()
marks.reverse()
print(marks)

# Q2 create a tuple of marks and add them

l = [1,2,3,4,5,6,7,8,9,]
print(sum(l))

# q3 count thee number of zeros in following tupple
tuple = (
    784, 231, 897, 456, 123, 678, 345, 890, 234, 765, 567, 789, 234, 654, 321, 987, 
    432, 876, 543, 210, 654, 876, 543, 109, 678, 345, 908, 657, 432, 876, 543, 789, 
    234, 987, 654, 321, 876, 543, 210, 678, 123, 765, 987, 654, 789, 234, 432, 678, 
    321, 654, 908, 345, 789, 876, 543, 210, 654, 987, 432, 876, 543, 210, 678, 765, 
    890, 123, 654, 876, 543, 987, 234, 678, 432, 876, 321, 908, 654, 543, 210, 678,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
)
print(tuple.count(0))