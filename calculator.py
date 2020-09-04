# VerAuthor : forrestMorrisey
# Version 1.3
# this version has loop back, ValueError checking, and removes early exit options

def _welcome_():
    print("""
    WELCOME TO CALCULTOR
    Beep Boop + - * / Math JA """)

def _calculate_():
    quitChk = "y" #Preassigned

    while quitChk == "y": #true
        operation = input(str("""
        Please type in the math operation you would like to complete
        + for addition
        - for subtraction
        * for multiplcation
        / for division
        ** for power
        % modulo
        Operation Type:
        """))

        while operation not in {"+", "-", "*", "/", "**", "%"}:
            operation = input(str("Please enter a valid math operation:  "))
      
        else:
            while True: #Requests the user for a number
                try:
                    number_1 = float(input('Enter your first number: '))
                    number_2 = float(input('Enter your second number: '))
                    break
                except ValueError: #Checks if input is valid
                    print("""============
                    Oops! That was not a valid number! Please try again ...""")
            
            ### Runs calculations
            if operation == '+':    # Addition
                print('{} + {} = ' .format(number_1, number_2))
                print(number_1 + number_2)

            elif operation == '-':  # Substraction

                print('{} - {} = ' .format(number_1, number_2))
                print(number_1 - number_2)

            elif operation == '*':  # Multiplication
                print('{} * {} = ' .format(number_1, number_2))
                print(number_1 * number_2)
            
            elif operation == '/':  # Division
                print('{} / {} = ' .format(number_1, number_2))
                print(number_1 / number_2)

            elif operation == '**': # POWAHAHAH
                print('{} ** {} = ' .format(number_1, number_2))
                print(number_1 ** number_2)

            elif operation == '%': # Modulo
                print('{} % {} = ' .format(number_1, number_2))
                print(number_1 % number_2)
            
            else: # Unnessary as input has already been checked, but we can't be too careful amirte?
                print("You have not typed in a valid operator, please run the program again!")

            ### Checks to run program again
            quitChk = input(str("Solve Another? y/n: "))
            quitChk = quitChk.lower()

            if quitChk == "y":
                continue

            else:
                print("I'm Outta Here")
                break

_welcome_()
_calculate_()


  

