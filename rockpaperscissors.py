print("Welcome to rock paper scissors game")
print("")

import random

def game():
    
    moves = ["rock", "paper", "scissors"]
    player_wins = 0
    computer_wins = 0
    playertotal = 0
    computertotals = 0

    for rounds in range (1, 4):
        print("Round", rounds)
        User = input ("Choose rock, paper or scissors: ")
        print(User)
        computer = random.choice(moves)
        print(computer)
    
        if User == "rock":
            if computer == "rock":
                print("You choose rock", "computer choose rock", "You tie")
            elif computer == "scissors":
                print("you choose rock", "computer choose scissors", "You win")
                player_wins += 1
            else:
                print("you choose rock", "computer choose paper", "You lose")
                computer_wins += 1    

        if User == "scissors":
            if computer == "rock":
                print("You choose scissors", "computer choose rock", "You Lose")
                computer_wins += 1
            elif computer == "scissors":
                print("you choose scissors", "computer choose scissors", "You Tie")
            else:
                print("you choose scissors", "computer choose paper", "You win")
                player_wins += 1

        if User == "paper":
            if computer == "rock":
                print("You choose paper", "computer choose rock", "You Win")
                player_wins += 1
            elif computer == "scissors":
                print("you choose paper", "computer choose scissors", "You Lose")
                computer_wins += 1
            else:
                print("you choose paper", "computer choose paper", "You Tie")        

    playertotal += player_wins
    computertotals += computer_wins
    print("")
    print ("player wins =", playertotal)
    print("computer wins =", computertotals)

    if playertotal == computertotals :
        print("Tie")
    elif playertotal > computertotals:
        print("You win")
    else:
        print("You lose")       
game()