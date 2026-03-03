import random

def compare_numbers(number, user_guess):
    ## your code here
    cowbull = [0, 0] # [cows, bulls]
    # Ensure both are treated as 4-character strings for comparison
    number = number.zfill(4)
    user_guess = user_guess.zfill(4)
    
    for i in range(len(number)):
        if user_guess[i] == number[i]:
            cowbull[1] += 1
        elif user_guess[i] in number:
            cowbull[0] += 1
    return cowbull

playing = True #gotta play the game
# Added .zfill(4) to ensure a number like 42 becomes "0042"
number = str(random.randint(0,9999)).zfill(4) #random 4 digit number
guesses = 0
# print number # We do not need this line of code.

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess! ") # raw_input is used in Python 2.x, but in Python 3.x, we should use input() instead.
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
