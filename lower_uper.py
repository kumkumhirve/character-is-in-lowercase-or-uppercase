'''Q7. Write a program to calculate whether character is in lowercase
or uppercase.'''

# Input character from user
char = input("Enter a single alphabet character: ")

# Check if it's a single alphabet character
if len(char) == 1 and char.isalpha():
    if char.islower():
        print(f"'{char}' is a lowercase letter.")
    else:
        print(f"'{char}' is an uppercase letter.")
else:
    print("Please enter a valid single alphabet character.")