"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

"""


# Zadání:
# 1) Program pozdraví uživatele a vypíše úvodní text

# 2) Program dále vytvoří tajné 4místné číslo
# (číslice musí být unikátní a nesmí začínat 0)

# 3) Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, 
# pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky

# 4) Program vyhodnotí tip uživatele

# 5) Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows 
# (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled na jednotné
# a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).
# 6) Po uhodnutí tajného čísla program vypíše počet pokusů a uplynulý čas.


import random
import time

# Print welcome message and instructions for the game
print('''Hi there!
I've generated a random 4 digit number for you.
\nLet's play a bulls and cows game.''')

def generate_secret_number():
    digits = list(range(10))  # Create a list of digits from 0 to 9
    random.shuffle(digits)  # Shuffle the list to create a random order
    return ''.join(map(str, digits[:4]))  # Join the first four digits as a string to form the secret number

def get_user_guess():
    while True:
        guess = input("Enter a number: ")  # Prompt the user to enter a number
        if len(guess) != 4:
            print("Číslo není 4 místné")  # Inform the user if the input number is not 4 digits long
        elif not guess.isdigit():
            print("Číslo obsahuje nepovolené znaky")  # Inform the user if the input contains non-numeric characters
        elif int(guess[0]) == 0:
            print("Číslo nesmí začínat nulou")  # Inform the user if the input starts with zero
        elif len(set(guess)) != 4:
            print("Číslo obsahuje duplicity")  # Inform the user if the input contains duplicate digits
        else:
            return list(guess)  # Convert the input string to a list of digits and return it

def evaluate_guess(secret_number, guess):
    bulls = 0
    cows = 0
    for i in range(0, 4):
        if guess[i] == secret_number[i]:
            bulls += 1  # Increment the count of bulls if the digit in the guess matches the digit in the secret number at the same position
        elif guess[i] in secret_number:
            cows += 1  # Increment the count of cows if the digit in the guess is present in the secret number but not at the same position
    return bulls, cows        

def spelling_cow(cow):
    if cow == 1:
        return "cow"
    else:
        return "cows"  # Return the appropriate plural form of "cow"

def spelling_bulls(bull):
    if bull == 1:
        return "bull"
    else:
        return "bulls"  # Return the appropriate plural form of "bull"

def main():
    secret_number = generate_secret_number()  # Generate the secret number
    attempts = 0   
    start_time = time.time()  # Record the start time of the game

    while True:
        guess = get_user_guess()  # Get the user's guess
        attempts += 1  # Increment the attempt count
        bulls, cows = evaluate_guess(secret_number, guess)  # Evaluate the guess
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")  # Print the number of bulls and cows

        if bulls == 4:  # If the user guessed all digits correctly
            end_time = time.time()  # Record the end time of the game
            elapsed_time = end_time - start_time  # Calculate the elapsed time
            print(f"Gratulujeme! Uhodli jste tajné číslo {secret_number} za {attempts} pokusů.")
            print(f"Čas potřebný k uhodnutí: {elapsed_time:2f} sekund.")  # Print the time taken to guess the secret number
            break

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly

