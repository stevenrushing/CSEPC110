grade = float(input("What is the grade percent? "))

if grade >= 90:
    letter_grade = "A"
elif grade >= 80:
    letter_grade = "B"
elif grade >= 70:
    letter_grade = "C"
elif grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

if grade >= 60 and grade < 95:
    while grade > 10:
        grade -= 10
    if grade >= 7:
        letter_grade += "+"
    elif grade < 3:
        letter_grade += "-"

print(f"You have earned a {letter_grade}")
if grade >= 70:
    print("Congratulations, you passed!")
else:
    print("I'm sorry, you have failed. ")