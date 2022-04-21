import random

class Die: 
	def roll(self):
		choose_die = random.randint(1,2)
		if choose_die == 1:
			return random.randint(1,6)
		else:
			return random.randint(1,8)

class Player(object):
    def _init_(self, name, score):
        self.name = name
        self.score = score    

    def getscore(self):
        return self.score
    
    def getname(self):
        return self.name

    def _str_(self):
        print("NAME: ", self.name , "\nSCORE: " , str(self.score))

class game(object):
	def _init_(self, playr, trails):
		self.trails = trails
		self.playr = playr
	def gaming(self):
		throw = 0
		score = 0
		die = Die()
		for i in range(self.trails):
			throw = die.roll()
			score = throw + score
		return score

	def _str_(self):
		return self.playr.getname() + str(self.score)		
        
print('-----------wElCoMe tO THIs GAMe--------------\n')

player_one_name = input("Enter player one name: ")
player_two_name = input("Enter player two name: ")
rounds_to_play = int(input("Enter number of rounds to play: "))

print('\n')

player_one = Player(player_one_name)
player_two = Player(player_two_name)

player_one_scr = game(player_one, rounds_to_play)
player_two_scr = game(player_two, rounds_to_play)


scrs = []
scrs.append(player_one_scr.gaming())
scrs.append(player_two_scr.gaming())

player_one.score(scrs[0])
player_two.score(scrs[1])

print(player_one, '\n')
print(player_two, '\n')

player_one_scoring = player_one.getscore()
player_two_scoring = player_two.getscore()

if player_one_scoring == player_two_scoring:
	print("It is a Draw")

if player_one_scoring > player_two_scoring:
	print(player_one.getname() + ' WINS')

if player_one_scoring < player_two_scoring:
	print(player_two.getname() + ' WINS')