# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) # The input is missing the 'int()' function.

exam_three = int(input("Input exam grade three: ")) # str() is wrong for this, since we need it as an integer to be able to calculate the grade based on a numeric value.
# Also, the variable name 'exam_3' is inconsistent with the other two exam variables, which are named 'exam_one' and 'exam_two'. It should be renamed to 'exam_three' for consistency.

grades = [exam_one, exam_two, exam_three] # The list of grades is missing commas between the entries
sum = 0
for grade in grades: # The variable 'grade' is not defined, it should be 'grades' to iterate through the list of grades.
  sum = sum + grade

avg = sum / len(grades) # The variable 'grdes' is misspelled, it should be 'grades' to get the correct length of the list of grades.

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: # There is no colon at the end of this line
    letter_grade = "B"
elif avg >= 70 and avg < 80: # The mark is not 69, it is 70. Also, the condition should be 'avg >= 70' to include the average of 70 in the 'C' grade range. Additionally, there is no colon at the end of this line.
    letter_grade = "C" # The 'elif' statement is missing a condition, and the letter grade should be "C" instead of "C'".
elif avg >= 60 and avg < 70: # The condition should be 'avg >= 60 and avg < 70'.
    letter_grade = "D"
else: # The 'elif' is meant to be an 'else' statement, since it is the catch-all for any average that is below 65.
    letter_grade = "F"

# for grade in grades:  We do not need to print this thrice, so we can remove this line of code. 
print("Exam: " + str(grades)) # It should have the three variables we defined for each grade, instead of just 'grade', which is not defined in this context. It should be 'exam_one', 'exam_two', and 'exam_three' to print each exam grade separately.

print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade == "F": #  The variable 'letter-grade' is not defined, it should be 'letter_grade' to check the letter grade assigned to the student. Also, the comparison should use '==' instead of 'is' for string comparison.
    print("Student is failing.")  # The print statement is missing parentheses. It should be: print("Student is failing.")
else:
    print("Student is passing.") # The print statement is missing parentheses. It should be: print("Student is passing.")

