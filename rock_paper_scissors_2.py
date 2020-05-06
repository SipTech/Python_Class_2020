from random import choice
from useful_functions import map_letter_to_full_word

leader_board = {
	"computer": 0,
	"you": 0
}
choices = ['Rock', 'Paper', 'Scissors']
valid_inputs = [
	"R",
	"Rock",
	"P",
	"Paper",
	"S",
	"Scissors",
	"Q",
	"Quit"
]

def get_user_choice(empty_list=[]):
	"""
	Get user input choice function..
	It MUST be a valid input from the valid_inputs list
	valid_inputs = ["R","Rock","Q","Quit"]
	:args list()
	:returns string
	"""
	user_choice = False
	while not user_choice:
		user_choice = input("""
    Please enter one of the following choices:
    R for Rock
	P for Paper
    S for Scissors
    Q for Quit: """
    ).title()
		if user_choice in empty_list:
			return user_choice
		else:
			user_choice = False

while True:
	computer_choice = choice(choices)
	user_pick = get_user_choice(valid_inputs)
	user_pick = map_letter_to_full_word(user_pick, valid_inputs)

	print(f"\nComputer: {computer_choice} <-> You: {user_pick}")
	if computer_choice == user_pick:
		leader_board["computer"] += 1
		leader_board["you"] += 1
		print("It's a tie....")

	if computer_choice == "Rock" and user_pick == "Scissors":
		leader_board["computer"] += 1
		print("Rock crushes Scissors....\nYou lose...\n")

	elif computer_choice == "Scissors" and user_pick == "Rock":
		leader_board["you"] += 1
		print("Rock crushes Scissors....\nYou win!!!\n")

	elif computer_choice == "Paper" and user_pick == "Rock":
		leader_board["computer"] += 1
		print("Paper covers Rock....\nYou lose...\n")

	elif computer_choice == "Rock" and user_pick == "Paper":
		leader_board["you"] += 1
		print("Paper covers Rock....\nYou win!!!\n")

	elif computer_choice == "Scissors" and user_pick == "Paper":
		leader_board["computer"] += 1
		print("Scissors cuts Paper....\nYou lose...\n")

	elif computer_choice == "Paper" and user_pick == "Scissors":
		leader_board["you"] += 1
		print("Scissors cuts Paper....\nYou win...\n")

	if user_pick == "Quit":
		print(f"""
			LEADER BOARD:
			Computer v You
			{leader_board['computer']}    :    {leader_board['you']}
		""")
		print("Thank you for playing :)\nSee you again next time.")
		break

	quit = input("Press [any key] to exit\nPress [enter] to replay..\n:")

	if len(quit) >= 1:
		print(f"""
			LEADER BOARD:
			Computer v You
			{leader_board['computer']}    :    {leader_board['you']}
		""")
		print("Thank you for playing :)\nSee you again next time.")
		break