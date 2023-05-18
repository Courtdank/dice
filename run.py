#!/usr/bin/env python3
from menu import Menu
import user

state = 1

def running():
	while True:
		usr = input(">  ")
		user.check_input(usr, state)


def main():
	menu = Menu()
	menu.main_menu()
	running()

if __name__ == '__main__':
	main()
