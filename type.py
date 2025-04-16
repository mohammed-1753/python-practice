a=31
t=type(a)
print(t)
#will print class int because 31 is an int similarly float and strings also
b="Mohammed"
t=type(b)
print(t)
#will print class str because mohammed is string
#if a nmber is also in double string like this "" then its class would be str not int or float

#if
a="31.2"
b=float(a) #Convert a string or number to a floating-point number, if possible.
t=type(b) #it will be a float class
print(t)
#step 1 a is str
#step 2 b converts a into float because its possible 
#step 3 t is type of b which is float
# In Python, you can use the built-in function `type()` to get the type of a