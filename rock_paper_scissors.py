#Play rock paper scissors between two players

play_again = True
while play_again==True:
    p1_move = input("Player 1's choice: ").lower().strip()
    p2_move = input("Player 2's choice: ").lower().strip()
    if p1_move == "rock":
        if p2_move == "rock":
            print("You Tied!")
        elif p2_move == "paper":
            print("Player 2 Wins!")
        else:
            print("Player 1 Wins!")
            
    elif p1_move == "paper":
        if p2_move == "rock":
            print("Player 1 Wins!")
        elif p2_move == "paper":
            print("You Tied!")
        else:
            print("Player 2 Wins!")
            
    else:
        if p2_move == "rock":
            print("Player 2 Wins!")
        elif p2_move == "paper":
            print("Player 1 Wins!")
        else:
            print("You Tied!")
            
    answer = input("Would you like to play again? ").lower().strip()
    if answer in ["yes", "ye", "y"]:
        continue
    else:
        break