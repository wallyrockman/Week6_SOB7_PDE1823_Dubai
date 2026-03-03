# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? ")) # We have to use '=', not '=='. Also, the 'input' function should be 'int(input())' to convert the user's input into an integer for comparison. 
                  # Additionally, there is a missing opening parenthesis before the string in the input function, and there is an extra closing parenthesis at the end of the line.

if year <= 1900: # Missing colon at the end of this line
    print ("Woah, that's the past!") # We have to use quotation marks, not an apostrophe.
elif year > 1900 and year < 2020: # The condition should use 'and' instead of '&&' for logical conjunction in Python.
    print ("That's totally the present!")
else: # We should use 'else'.
    print ("Far out, that's the future!!")
