
import random
print("Welcome to the Adopt Puppies program")
userName = input("Please enter your name here: ")
print("Hello" ,userName)
print("\n")

class Puppy():

    def __init__(self, name, age, size, breed):
        self.name = name
        self.size = size
        self.age = age
        self.breed = breed

    def bark(self):
        print(self.name, "is barking")

    def play(self):
        print(self.name,"is playing")

    def wag(self):
        print(self.name, "is wagging it tail")

    def smile(self):
        print(self.name, "is smiling at you") 

    def whimper(self):
        print(self.name, "is whimpering")

def game():
    puppies = []
    numPuppies = int(input("Please enter the number of puppies you want to adopt today: "))
    print(numPuppies ,"puppies it is !")
    print("\n") 

    print("You will be asked a series of questions to get information on each puppy you`d like to adopt")

    for i in range (numPuppies):
        print("For puppy number", numPuppies)
        numPuppies -= 1
    
        name = input("Please enter a name for the puppy: ")
        age = input("Plase enter a age in weeks for the puppy: ")
        size = input("Please enter a size for the puppy ~small, medium, large~: ")
        breed = input("Enter the breed of puppy you want: ")
        puppy = Puppy(name, age, size, breed)
        puppies.append(puppy)
        print("the puppy is ", puppy.name, ",", puppy.age, "weeks old,", puppy.size, "in size and its breed is a", puppy.breed, ".")


    confirm = input("is the above information correct?, type yes or no: ")
    if confirm == 'no':
        print("Thank you for using this service!")
    elif confirm == 'yes':
        print("Thank you for using this service!")
        onePuppy = random.choice(puppies)
        print("\n")
        onePuppy.bark()
        print(onePuppy.name, 'wants to play with you')
        play = input("will you play, yes/no ?: ")
        while play.lower() == 'no':
            onePuppy.whimper()
            play = input("will you play, yes/no ?: ")
        if play.lower() == 'yes':
            onePuppy.play()
            onePuppy.wag()
            onePuppy.smile()   
          
game()   



