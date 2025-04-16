# q1
class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
# This is a special box called programmer.
# A box is like a toy that can do things.
class programmer:
    company = "Microsoft"  # This is the name of the place where the programmer works.

    # This is a magic door that opens when we make a new programmer.
    def __init__(self, name, salary, pin):
        self.name = name  # This is the name of the programmer.
        self.salary = salary  # This is how much money the programmer gets.
        self.pin = pin  # This is a secret number for the programmer.

# Now we are making a new programmer named Mohammed.
p = programmer("Mohammed", 500000, 390019)
# Let's show Mohammed's name, where he works, how much money he gets, and his secret number.
print(p.name, p.company, p.salary, p.pin)

# Now we are making another programmer named Rohan.
r = programmer("rohan", 500000, 390019)
# Let's show Rohan's name, where he works, how much money he gets, and his secret number.
print(r.name, r.company, r.salary, r.pin)

# Now we have another special box called calculator.
# This box helps us do math.
class calculator:
    # This is a magic door that opens when we make a new calculator.
    def __init__(self, n):
        self.n = n  # This is the number we want to play with.

    # This magic trick will help us find the square of the number.
    def square(self):
        # This will show the square of the number (like 4 times 4).
        print(f"The square is {self.n * self.n}")  # Corrected to show the square, not cube.

# Now we are making a new calculator with the number 4.
a = calculator(4)
# This will find the square of 4 and show it.
a.square()

#q3

class attribute:
    a=4

o= attribute()
print(o.a)

#q4
class Train:
    def __init__(self, train_number, train_name, total_seats, base_fare):
        # Initializing the train details
        self.train_number = train_number
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats  # Initially, all seats are available
        self.base_fare = base_fare
        self.booked_tickets = 0

    def book_ticket(self, num_tickets):
        """
        Books tickets if there are enough available seats.
        """
        if num_tickets <= self.available_seats:
            self.booked_tickets += num_tickets
            self.available_seats -= num_tickets
            print(f"Successfully booked {num_tickets} tickets for train {self.train_name} ({self.train_number}).")
        else:
            print(f"Not enough seats available! Only {self.available_seats} seats left.")

    def get_status(self):
        """
        Returns the status of the available seats.
        """
        return f"Train {self.train_name} ({self.train_number}) has {self.available_seats} seats available."

    def get_fare_info(self):
        """
        Returns the base fare for the train.
        """
        return f"Base fare for train {self.train_name} ({self.train_number}) is Rs. {self.base_fare}."

# Example Usage
train1 = Train(101, "Rajdhani Express", 100, 1500)
train2 = Train(202, "Shatabdi Express", 80, 1000)

# Check the status of available seats
print(train1.get_status())
print(train2.get_status())

# Book some tickets
train1.book_ticket(10)
train2.book_ticket(50)

# Check the status again after booking
print(train1.get_status())
print(train2.get_status())

# Get fare information
print(train1.get_fare_info())
print(train2.get_fare_info())

