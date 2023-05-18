from dice import Dice
from menu import Menu


def check_input(usr, state):
	if state == 1:
		check_menu_input(usr)
	elif state == 2:
		check_dice_input(usr)

def check_menu_input(usr):
	if usr == '1':
		menu = Menu()
		menu.main_menu()
	elif usr == '2':
		exit()
	else:
		invalid_input()

def check_dice_input(usr, state):
	options = ['D4','D6','D8','D10','D12','D20']
	if usr.upper() not in options:
		invalid_input()
	else:
		pass #return the input to call the dice roll

def invalid_input():
	print('Invalid input! Try again...\n')
