def avg():
    # Prompt the user to enter the first number and convert it to an integer
    a = int(input("Enter your number: "))
    
    # Prompt the user to enter the second number and convert it to an integer
    b = int(input("Enter your number: "))
    
    # Prompt the user to enter the third number and convert it to an integer
    c = int(input("Enter your number: "))

    # Calculate the average of the three numbers
    average = (a + b + c) / 3
    
    # Print the calculated average
    print(average)  # Print the value of average

# Call the avg function to execute the code
avg()
