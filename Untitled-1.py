import random

def guessgame() :
    print("welcome to guess the word game where you`ll be entering letters to form a word")

    wordbank = ["while", "yatch", "boat", "birds"]
    computer = random.choice(wordbank)

    correct_letter=["-"]*len(computer)
    blanks= "".join(correct_letter)
    print('\n')

    print(blanks)
    print("Here is a hint, the word is", len(computer), "letters long") 

    passes = 6
    while passes > 0:
        passes -= 1
        user = input("guess a letter: ")
        if user in computer:
            for index in range(len(computer)):
                if computer[index] == user:
                    correct_letter[index] = user
                    blanks= "".join(correct_letter)
            print(blanks)
            print("Your guess was correct!") 
        else:
            print("Your guess was incorrect!")
            print("You have", passes, "passes left")

        print("\n")
        if blanks == computer:
            print("You win")
            break
        elif passes == 0:
            print("You lost, Game over!")    
guessgame()        