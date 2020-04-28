from random import randint

# random number equalsTo random integer between (0, 20)
random_number = randint(0, 20)
# user guess equals None
user_guess = None
# while user guess is not equal to random number
while user_guess != random_number:
	# get input user guess between 0 and 20 and cast the guess to integer
	user_guess = int(input("Please guess/enter a number between {0} and {1}: ".format(0, 20)))
	# check if user guess is between 0 and 20
	if 0 <= user_guess <= 20:
		# if user input equalsTo random number
		if user_guess == random_number:
			# print well done the number is x
			print("Well done the number is: {0}".format(random_number))
			# user won the game, let's break the loop
			break
		# if user guess is less than random number
		elif user_guess < random_number:
			# print your guess is too low
			print("Your guess {0} is too low..".format(user_guess))
		# if user guess is greater than random number
		elif user_guess > random_number:
			# print your guess is too high
			print("Your guess {0} is too high..".format(user_guess))
		# let's give the player an option to quit the game
		quit_game = input("If you wish to give up, type in (any value) or hit (enter) to try again: ")
		# If quit is not empty, it means user gave up otherwise the game continues
		if quit_game:
			# Upon exit, let's reveal or random number to the user
			print("Oops!! My random number was {0}...\nSad to see you give up :( \nI hope we play again soon :)".format(random_number))
			# To end the game by breaking the loop
			break
	# If we get here it means user input is not an interger between 0 and 20
	else:
		# Notify the user of their offence
		print("{0} is invalid!!!\nPlease make sure, your input is an integer between 0 and 20".format(user_guess))
