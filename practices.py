name = input("Enter your name :" )
print(f"GOOD MORNING {name} ")

letter = '''Dear <|Name|>
            you are selected 
             <|Date|>'''
print(letter.replace("<|Name|>","Mohammed").replace("<|Date|>","26/11/2001"))

name="mamamama   jscnejecnsjs makichuytnkjbvds"
print(name.find(" "))
# .find syntax finds somethin in container you want for example here it finds " " in name

#2 practice of lists and methods

friends = ["bhoot", "Chudail" , "Dayan" , "Hanuman", "khilji"]
print(friends)
friends.append("Moghal") #append adds a string to list at the end 
print(friends)
friends.reverse() #reverese the list by this method
print(friends)
friends.sort()#sorts the lists
print(friends)

l1=[1,2,3,4,5,7,8,9]
l1.insert(3,3.3369) #inserts 3.3369 at 3rd place ie after 3 in this case
print(l1)

print(l1.pop(3))

# lists are mutable
# strings are immutable
# so are tupples