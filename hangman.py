import random

#Hangman game

"""
Choose random word from a list of words

Ask user to guess a letter

If letter is in word, print the letter in the correct position, underscores for the rest

If letter is not in word, print "Wrong" and save the letter to a list of used letters

If the user finishes guessing the word, print "You win!"

If the user runs out of guesses, print "You lose!"
"""

word_list = [
    "apple", "banana", "carrot", "dog", "elephant", "fish", "guitar", "house", "igloo", "jazz",
    "kangaroo", "lemon", "monkey", "nut", "orange", "piano", "queen", "rabbit", "sun", "tiger",
    "umbrella", "violin", "watermelon", "xylophone", "yacht", "zebra", "airplane", "beach", "cat",
    "dolphin", "earth", "fire", "garden", "hat", "island", "jungle", "koala", "laptop", "mountain",
    "ninja", "ocean", "penguin", "quilt", "rainbow", "sailboat", "tree", "unicorn", "volcano", "whale",
    "xylophone", "yoga", "zeppelin"
]



def main():
    """
    Main function, calls hangman() and asks user if they want to play again
    """
    hangman()
    while True:
        play_again = input("Would you like to play again? (y/n): ").lower().strip()
        if play_again in ["y", "yes", "ye"]:
            hangman()
        else:
            exit()
    

def hangman():
    """
    Main game loop
    """
    ALLOWED_GUESSES = 8
    word = random.choice(word_list)
    guesses = 0
    revealed = "_" * len(word)
    used_letters = []
    
    while True:
        print(revealed)
        input_letter = get_input("Guess a letter: ", used_letters)
        used_letters.append(input_letter)
        
        if input_letter in word:
            revealed = "".join([input_letter if input_letter == word[i] else revealed[i] for i in range(len(word))])
            if revealed == word:
                print(f"You win! You found the correct word, {word}!")
                break
        else:
            guesses += 1
            print(f"Wrong! You have {ALLOWED_GUESSES - guesses} wrong guesses left!")
            if guesses == ALLOWED_GUESSES:
                print(f"You lose! The word was {word}")
                break


def get_input(message, used_letters):
    """
    Get and validate input from user, returns a character that is not in used_letters
    """
    while True:
        input_letter = input(message).lower().strip()
        if len(input_letter) == 1 and input_letter.isalpha():
            if input_letter not in used_letters:
                return input_letter
            else:
                print("You already guessed that letter!")
                continue
        else:
            print("Please enter a single letter")
            continue


if __name__ == "__main__":
    main()