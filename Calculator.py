########################################################################################################
##
## 10/05/2023
##
## This code creates a simple python based calculator. I'm learning python, and this is a good
##  coding exercise.
##  Created with help from https://www.programiz.com/python-programming/examples/calculator
##
## First Written 10/05/2023 by Yogi Patel.
##
##  Change Log:
##
##  Version | Authour               | Change
##  -------------------------------------------------------
##          |                       |
##    1.0   | Yogi Patel            |
##
##
#######################################################################################################


# First we create a set of functions

# Function to add 2 numbers
def add(x, y):
    return x + y

# Function to subtract 2 numbers
def subtract(x, y):
    return x - y

# Function to multiply 2 numbers
def multiply(x, y):
    return x * y

# Function to divide 2 numbers
def divide(x, y):
    return x / y

print ("Select Operation\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")



while True:
    #Get input from user
    choice = input("Enter Choice (1, 2, 3, or 4): ")

    #Check it's a correct choice
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter Second number: "))
        except ValueError:
            print("Dumbass. That's not a number is it? Enter a number: ")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        # Check if user wants another calculation
        # break loop if not
        next_calc = input("Do antoher calc? (y/n): ")
        if next_calc == "n":
            break
        else:
            print("Let's go again")
    

