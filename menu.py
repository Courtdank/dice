import os

class Menu:
	def __init__(self):
		self.title = "******Dice Roller******\n"
		self.main =  "1.Start\n2.Quit\n"
		self.dice = "D4 D6 D8 D10 D12 D20"

	def main_menu(self):
		os.system('clear')
		print("{}{}\n".format(self.title, self.main))

	def dice_menu(self):
		os.system('clear')
		available_dice = "{}Available dice:~ {}\n".format(self.title, self.dice)
		options = "Select a dice from the options above  :~'D6'\n"
		print(available_dice, options)

	#def clear_screen():
		#os.system('clear')