from random import choice

leader_board = {
  "computer": 0,
  "you": 0
}
choices = ["Rock", "Paper", "Scissors"]
valid_inputs = ["R","Rock", "P", "Paper", "S", "Scissors", "Q", "Quit"]

def get_user_choice(valid_user_choices=[]):
  """
  Get user input choice function..
  It MUST be a valid input from the valid_inputs list
  :args list()
  :returns void
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
    if user_choice in valid_user_choices:
      return user_choice
    else:
      user_choice = False


while True:
  # get psaudo random computer choice
  computer_choice = choice(choices)
  # User choice can either be a letter or a word
  user_pick = get_user_choice(valid_inputs)
  """
  Because user choice can either be a letter or a word,
  I created an anonymous function to select a word starting with
  a letter x that is more than one character in length.
  This way we pick the corresponding word using the given letter.
  """
  user_pick = list(filter(lambda x: x.startswith(user_pick) and len(x) > 1, valid_inputs))[0]

  print(f"\nComputer: {computer_choice} <-> You: {user_pick}")
  if computer_choice == user_pick:
    leader_board["computer"] += 1
    leader_board["you"] += 1
    print(f"It's a tie....\n")
  
  if computer_choice == "Rock" and user_pick == "Scissors":
    leader_board["computer"] += 1
    print("Rock crushes Scissors....\nYou lose...\n")

  if computer_choice == "Scissors" and user_pick == "Rock":
    leader_board["you"] += 1
    print("Rock crushes Scissors....\nYou win!!!\n") 
  
  if computer_choice == "Paper" and user_pick == "Rock":
    leader_board["computer"] += 1
    print("Paper covers Rock....\nYou lose...\n")
  
  if computer_choice == "Rock" and user_pick == "Paper":
    leader_board["you"] += 1
    print("Paper covers Rock....\nYou win!!!\n") 

  if computer_choice == "Scissors" and user_pick == "Paper":
    leader_board["computer"] += 1
    print("Scissors cuts Paper....\nYou lose...\n")

  if computer_choice == "Paper" and user_pick == "Scissors":
    leader_board["you"] += 1
    print("Scissors cuts Paper....\nYou lose...\n")

  if user_pick == "Quit":
    print(f"""
      LEADER BOARD:
      Computer v You
      {leader_board['computer']}    :    {leader_board['you']}
      \n
    """)
    print("Thank you for playing :)\nSee you again next time.")
    break   
  
  quit = input("Press [any key] to exit\nPress [enter] to replay..\n:")
  
  if len(quit) >= 1:
    print(f"""
      LEADER BOARD:
      Computer v You
      {leader_board['computer']}    :    {leader_board['you']}
      \n
    """)
    break
      