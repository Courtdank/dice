import random

class Dice:
	def __init__(self, n):
		self.n = n
		self.x = self.n ** 2
		self.y = self.n % self.x

	def roll_dice(self):
		result = random.randint(1, self.y)
		print(result)

