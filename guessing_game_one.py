import random

#Guessing game for numbers between 1 and 9

def main():
    """
    Main function for guessing game
    """
    print("Guessing Game! Type 'exit' to quit")
    while True:
        rand = random.randint(1,9)
        guess = 0
        guess_count = 0
        
        while guess != rand:
            guess = get_input("Guess a number between 1 and 9: ")
            guess_count += 1
            if guess == rand:
                print(f"You got it! It took you {guess_count} guesses!")            
                break
            elif guess < rand:
                print("Too Low!")
            else:
                print("Too High!")
                
        if input("Play Again? ").lower().strip() in ["yes", "ye", "y"]:
            continue
        else: 
            break
        

def get_input(message):
    """
    Get and validate input from user, returns int between 1 and 9
    """
    while True:
        try:
            user_input = int(input(message))
            if user_input in range(1,10):
                return user_input
            else:
                print("Please enter a number between 1 and 9")
        except ValueError:
            if input("Are you sure you want to quit? ").lower().strip() in ["yes", "ye", "y"]:
                exit()
            else:
                continue
        
if __name__ == "__main__":
    main()
    