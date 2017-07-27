import sys
playerOne = int(input("Player one please choose '1 = rock', '2 = paper', or '3 = scissors': "))
playerTwo = int(input("Player two please choose '1 = rock', '2 = paper', or '3 = scissors': "))
if playerTwo == 3 and playerOne == 1:
    print("Player Two wins!")
    sys.exit("Game Over")
if playerTwo == 1 and playerOne ==3:
    print("Player One wins!")
    sys.exit("Game Over")
if playerOne == playerTwo:
    print("The game is a draw.")
if playerOne > playerTwo:
    print("Player One has won the game.")
if playerTwo > playerOne:
    print("Player Two has won the game.")
    
