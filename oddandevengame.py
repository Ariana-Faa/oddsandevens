import random

# Functions go here


# yes_no function
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter yes or no")


# instructions function
def instructions():
    statement_generator("How to Play", "+")
    print()
    print("Choose either odds or evens")
    print()
    print("Each round you will enter a number between 1 and 10")
    print()
    print("The computer will generate a random number between 1 and 10")
    print("If the total of both numbers is even and you chose even you win the round")
    print("But if the total of both numbers is odd you lose")
    print("We will play a total of 5 rounds")
    print("If you win 3 rounds you win a prize")
    print()
    print("Hint: to quit while you are ahead, type 'xxx' instead of")
    print("pressing <enter>")
    return ""


# odd_even function
def odd_even(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "even" or response == "e":
            response = "even"
            return response

        elif response == "odd" or response == "o":
            response = "odd"
            return response

        else:
            print("Please pick odd or even")


# num_check function
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            response = int(input(question))

            # ask the question
            if low < response <= high:
                return response

            # if the amount is too low / too high give...
            else:
                print(error)

        except ValueError:
            print(error)


# statement_generator function
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# number_pick function
def number_pick(question):

# Main Routine goes here
statement_generator("Welcome to the Odds and Evens Game", "*")
print()

# Ask for users name
username = input("What is your username?")
print()

# Ask user if they have played before
played_before = yes_no("Hello {}! Have you played this game before?".format(username))
print()

# if no, show instructions and if yes, play the game
if played_before == "no":
    instructions()
print()

# Ask if user wants to be odd or evens
odd_even = str(input("{}, do you want to be odds or evens?".format(username)))
print()

statement_generator("Let's get Started...", "*")
print()

# Round 1. User selects a number in range
statement_generator("Round 1", "|")
print()

number_pick = int(input("Pick a number between 1 and 10"))
# Add numbers together


# Print winner (ex. "You chose 1, I chose 3, the total is 4. You are odds 'name', you lose")


# Store results of each round in list


# At end print out results of each round and state who won the most rounds


# If the user wins print that they have won a choice from a prize


# show the list


# user chooses a random number to decide their prize


# Tell the user what they won
