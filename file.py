# Import the random module to generate random numbers
import random  

# Define a function named 'game'
def game():  
    # Print a message indicating the game has started
    print("You are playing the game..")  
    # Generate a random score between 1 and 62
    score = random.randint(1, 62)  

    # Fetch the hiscore
    # Open the file 'hiscore.txt' for reading
    with open("hiscore.txt") as f:  
        # Read the contents of the file and store it in 'hiscore'
        hiscore = f.read()  
        # Check if 'hiscore' is not an empty string
        if(hiscore != ""):  
            # Convert 'hiscore' to an integer
            hiscore = int(hiscore)  
        else:  # If 'hiscore' is empty
            # Set 'hiscore' to 0
            hiscore = 0  

    # Print the player's score
    print(f"Your score: {score}")  
    # Check if the current score is greater than the hiscore
    if(score > hiscore):  
        # Open 'hiscore.txt' for writing
        with open("hiscore.txt", "w") as f:  
            # Write the new hiscore to the file as a string
            f.write(str(score))  

    # Return the current score
    return score  

# Call the 'game' function to execute the game
game()
