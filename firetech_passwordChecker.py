#!/usr/bin/env python3

# Define a global variable password (plain text so not very secure)
password = ""

# Returns 1 if password matches criteria
def validate_password(password):
    # First check if it has the correct length
    if len(password) < 6 or len(password) > 32:
        print("Your password must be between 6 and 32 characters long")
        return 0
    has_upper = 0
    for char in password:
        # Check each character to see if its a space
        if char == " ":
            print("Please don't use whitespaces")
            return 0
        elif char.isupper():
            # Additionally, if any character is uppercase, set the value of has upper to 1
            has_upper = 1
        # If none of the characters were uppercase, result is invallid
        if has_upper == 0:
            print("You need at least 1 uppercase character")
            return 0
        # If everything is valid, result is valid
        return 1


# Define the initial user prompt and return the user's input
def ask_input():
    print("Please enter a password containing between 6 and 32 characters. Use at least one uppercase letter and no whitespace(spaces/tabs...)")
    x = input("> ")
    return x

# Helper function to prompt the user for a number. Used when asking for various options
# TODO: change so that you can insert the options as arguments and the check is done here
def get_option():
    # While the user enters false input (e.g: not a number), prompt for input
    while True:
        try:
            choice = int(input("> "))
        except ValueError:
            print("Please enter a valid option")
            continue  # return to start of loop
        else:
            # The user entered a correct option, exit the loop
            return choice

# Function to verify the password


def verify_password():
    global password
    print("please enter the 1st character of your password")
    first_char = input("> ")
    if first_char != password[0]:
        print("Incorrect")
    else:
        print("Correct")


# Lists the available menu options
def list_options():
    print("What would you like to do? Select an option (1 or 2) from the following:")
    print(" \t 1.Verify my password \n\t 2.Exit")
    choice = get_option()
    while choice not in [1, 2]:
        print("Please enter a valid option (1 or 2)")
        choice = get_option()

    if choice == 1:
        print("Verification..")
        verify_password()
    elif choice == 2:
        print("Exiting..")


def main():
    valid = 0
    while not valid:
        global password
        password = ask_input()
        valid = validate_password(password)
    print("Congratulations, you have entered a correct password! \n")
    list_options()


if __name__ == '__main__':
    main()
