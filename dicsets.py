# This dictionary stores the number of subscribers for different users
subscribers={
    "me": 10000,  # Number of subscribers for "me"
    "you": 3000,   # Number of subscribers for "you"
    "them": 2000,  # Number of subscribers for "them"
    "alpha": 40000000  # Number of subscribers for "alpha"
}

# Print the number of subscribers for "alpha"
print(subscribers["alpha"])

# Print the entire subscribers dictionary
print(subscribers)

#sets
#s=()#will create an empty set .dont use s={} for empty set and to create a set always use s={}
s=(1,2,3,4,5,6,7,8,9,10,5,5,5,5,6,7,6,7,) #this is tuple
print(s)
s={1,2,3,4,5,6,7,8,9,10,5,5,5,5,6,7,6,7,}
print(s) #this is set ,set does not repeat numbers alloted.


# methods
s1={1,2,3,4,5,5,6}
s2={6,7,8,9,0,10}
print(s1.union(s2)) #prints both the sets combine in union
print(s1.intersection(s2)) #Return a new set with elements common to the set and all others.ie 6