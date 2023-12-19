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


print('''Hi there!
I've generated a random 4 digit number for you.
\nLet's play a bulls and cows game.''')


def generate_secret_number():
    digits = list(range(10)) # výběr čísel 0 až 9
    random.shuffle(digits) # promíchá
    return ''.join(map(str, digits[:4])) # vybere poslední 4 čísla

def get_user_guess():
    while True:
        guess = input("Enter a number: ")
        if len(guess) != 4:
            print("Číslo není 4 místné")
        elif not guess.isdigit():
            print("Číslo obsahuje nepovolené znaky")
        elif int(guess[0]) == 0:
            print("Číslo nesmí začínat nulou")
        elif len(set(guess))!=4:
            print("Číslo obsahuje duplicity")
        else:
            return list(guess)

def evaluate_guess(secret_number, guess):
    bulls = 0
    cows = 0
    for i in range(0,4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows        

def spelling_cow(cow):
    if cow == 1:
        return "cow"
    else:
        return"cows"


def spelling_bulls(bull):
    if bull == 1:
        return "bull"
    else:
        return "bulls"

def main():
    secret_number = generate_secret_number()
    attempts = 0   
    start_time = time.time()

    while True:
        guess = get_user_guess()
        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

        if bulls == 4:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Gratulujeme! Uhodli jste tajné číslo {secret_number} za {attempts} pokusů.")
            print(f"Čas potřebný k uhodnutí: {elapsed_time:2f} sekund.")
            break

if __name__ == "__main__":
    main()
