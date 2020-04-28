from random import randint


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def guessing_game(start=0, end=20):
    """
    A function for playing a guessing game with users.
    This function accepts to integers, a start value and an end value.
    When invoked the function will keep prompting the player to guess a pseudo random
    generated value.
    The game continues until either the user correctly guesses the value
    or quits the game.
    :return: void
    """
    # random number equalsTo random integer between (start, end)
    random_number = randint(start, end)
    # user guess equals -1
    user_guess = -1
    # while user guess is not equal to random number
    while user_guess != random_number:
        # lets try to get a valid integer from user
        try:
            # get input user guess between start and end and cast the guess to integer
            user_guess = int(input("Please guess/enter a number between {0} and {1}: ".format(start, end)))
        # if the value entered cannot be cast into an it let's except this value error
        # and simply give the user another chance to try again.
        except ValueError as err:
            print("{0}Please enter a valid integer...\n{1}{2}".format(BColors.FAIL, err, BColors.ENDC))
        # check if user guess is between start and end
        if start <= user_guess <= end:
            # if user input equalsTo random number
            if user_guess == random_number:
                # print well done the number is x
                print("{0}Well done the number is: {1}{2}".format(BColors.OKGREEN, random_number, BColors.ENDC))
                # user won the game, let's break the loop
                break
            # if user guess is less than random number
            elif user_guess < random_number:
                # print your guess is too low
                print("{0}Your guess {1} is too low..{2}".format(BColors.FAIL, user_guess, BColors.ENDC))
            # if user guess is greater than random number
            elif user_guess > random_number:
                # print your guess is too high
                print("{0}Your guess {1} is too high..{2}".format(BColors.FAIL, user_guess, BColors.ENDC))
            # let's give the player an option to quit the game
            quit = input("{0}If you wish to give up, type in (any value) or hit (enter) to try again: {1}".format(BColors.WARNING, BColors.ENDC))
            # If quit is not empty, it means user gave up otherwise the game continues
            if quit:
                # Upon exit, let's reveal or random number to the user
                print("{0}Oops!! My random number was {1}...\nSad to see you give up :( \nI hope we play again soon :){2}".format(BColors.FAIL, random_number, BColors.ENDC))
                # To end the game by breaking the loop
                break
        # If we get here it means user input is not a valid integer
        else:
            # Notify user of this offence
            print("{0}{1} is invalid!!!!\nPlease make sure, your input is an integer between {2} and {3}{4}".format(BColors.FAIL, user_guess, start, end, BColors.ENDC))


if __name__ == "__main__":
    # lets invoke/call our function with two optional integer arguments
    guessing_game(0, 1000)