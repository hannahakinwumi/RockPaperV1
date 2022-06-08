from random import randint

moves = ["rock", "paper", "scissors"]

while True:
    computer = moves[randint(0,2)]
    player = input("rock, paper or scissors? (or end the game) ").lower()
    if player =="end the game":
        print("The game has ended.")
        break 
if player == computer:
 print("Tie")
elif player =="rock":
 if computer =="paper":
            print("You lose!", computer, "beats", player)
else:
            print("You win!", player, "beats", computer)
        
