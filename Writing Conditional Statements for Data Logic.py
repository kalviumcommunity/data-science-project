# 1. Basic if statement
number = 10

if number > 5:
    print("Number is greater than 5")


# 2. if - else statement
age = 16

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# 3. if - elif - else statement
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 4. Logical operator: AND
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote (AND condition)")


# 5. Logical operator: OR
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It is the weekend")


# 6. Logical operator: NOT
logged_in = False

if not logged_in:
    print("Please login to continue")