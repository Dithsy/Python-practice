import random

class Die: 
	def roll(self):
		choose_die = random.randint(1,2)
		if choose_die == 1:
			return random.randint(1,6)
		else:
			return random.randint(1,8)

class Player(object):
	def __init__(self, name):
		self.name = name 

	def score(self, score):
		self.score = score

	def playerscore(self):
		return self.score

	def playername(self):
		return self.name

	def __str__(self):
		return 'NAME: ' + self.name + '\nTOTALSCORE: ' + str(self.score)

class Game(object):
	def __init__(self, playr, rounds):
		self.rounds = rounds
		self.playr = playr
	
	def gaming(self):
		current_roll = 0
		total_score = 0
		die = Die()
		for i in range(self.rounds):
			current_roll = die.roll()
			print("Round", i+1)
			print(self.playr.playername(), current_roll, '\n')
			total_score = current_roll + total_score
		return total_score

	def __str__(self):
		return self.playr.playername() + str(self.score)		
        
print('-----------wElCoMe tO dIcE GAMe--------------\n')

player1_name = input("Enter player one name: ")
player2_name = input("Enter player two name: ")
rounds_to_play = int(input("Enter number of rounds to play: "))

print('\n')

player1 = Player(player1_name)
player2 = Player(player2_name)

player1_score = Game(player1, rounds_to_play)
player2_score = Game(player2, rounds_to_play)


player1.score(player1_score.gaming())
player2.score(player2_score.gaming())

print(player1,'\n')
print(player2, '\n')

player1_total = player1.playerscore()
player2_total = player2.playerscore()

if player1_total == player2_total:
	print("It is a Draw")

if player1_total > player2_total:
	print(player1.playername() + ' WINS')

if player1_total < player2_total:
	print(player2.playername() + ' WINS')