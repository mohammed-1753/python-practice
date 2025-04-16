import random

class MathQuizGame:
    def __init__(self):
        self.score = 0
        self.total_questions = 5

    def generate_question(self):
        # Randomly select two numbers and an operator
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*', '/'])

        # Depending on the operator, calculate the answer
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        elif operator == '*':
            answer = num1 * num2
        elif operator == '/':
            # Avoid division by zero
            num2 = random.randint(1, 10)
            answer = round(num1 / num2, 2)  # Round to 2 decimal places

        # Create the question
        question = f"What is {num1} {operator} {num2}?"
        return question, answer

    def start_game(self):
        print("Welcome to the Math Quiz Game!")
        print(f"You will be asked {self.total_questions} questions. Let's start!\n")

        for i in range(self.total_questions):
            question, correct_answer = self.generate_question()
            print(f"Question {i + 1}: {question}")
            
            # Get player's answer
            try:
                player_answer = float(input("Your answer: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            # Check if the answer is correct
            if player_answer == correct_answer:
                print("Correct! Well done.\n")
                self.score += 1
            else:
                print(f"Incorrect! The correct answer was {correct_answer}.\n")

        # Game over
        print(f"Game Over! Your final score is: {self.score} out of {self.total_questions}")

# Start the game
game = MathQuizGame()
game.start_game()
