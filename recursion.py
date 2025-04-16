def factorial(n):
    """
    Calculate the factorial of a given number n using recursion.

    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    It is denoted as n! and is defined as:
    - n! = n * (n-1)! for n > 1
    - 0! = 1 and 1! = 1 (base cases)

    Parameters:
    n (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the number n.
    """
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    return n * factorial(n - 1)  # Recursive case: n * factorial of (n-1)

# Get user input for the number to calculate the factorial of
n = int(input("Enter the number you need the factorial of: "))

# Print the result of the factorial calculation
print(f"The factorial of {n} is {factorial(n)}")
