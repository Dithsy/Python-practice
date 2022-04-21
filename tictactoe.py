
import random

print("welcome to tic tac toe game between you and the computer. You will be X while the computer will be O")
print("This is the board!", "You will be playing first!")

board = {1:'1', 4:'4', 7:'7',
         2:'2', 5:'5', 8:'8',
         3:'3', 6:'6', 9:'9'}

def displayHelper(num):
    return board[num]

def displayBoard():
    print(displayHelper(1) +" "+ displayHelper(4) +" "+ displayHelper(7))
    print(displayHelper(2) +" "+ displayHelper(5) +" "+ displayHelper(8))
    print(displayHelper(3) +" "+ displayHelper(6) +" "+ displayHelper(9))

def checkTripple(num1, num2, num3):
    return board[num1] == board[num2] and board[num1] == board[num3]

def checkwinner():
    return checkTripple(7, 8, 9) or checkTripple(4, 5, 6) or checkTripple(1, 2, 3) or checkTripple(1, 4,7) or checkTripple(2, 5, 8) or checkTripple(3, 6, 9) or checkTripple(7, 5, 3) or checkTripple(1, 5, 9)              


def game():
    availablePos = [1, 2, 3, 4, 5, 6, 7, 8, 9 ] 
    turn = 'X'
    count = 0
    rounds = 9


    while rounds > 0:
        rounds -= 1
        displayBoard()
        if turn == 'X':
            print("\n")
            print("It`s your turn")
            user = int(input("Please enter a number between 1-9: "))

            if board[user] != 'X' and board[user] != 'O':
                board[user] = turn
                availablePos.remove(user)
                count += 1
            else:
                print("That place is already filled.\nuser to which place?")
                continue
        else:
            print("\n")
            print("It`s the computers turn")
            computer = random.choice(availablePos)
            board[computer] = turn
            availablePos.remove(computer)
            count += 1

        if count >= 5:
            if checkwinner():
                displayBoard()
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            
        if count == 9:
            print("game over! its a tie")
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'   

game()        
