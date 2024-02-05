"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Olina Savčuková
email: olinkasavcuk@gmail.com
discord: olinasavcukova_13648
"""
import random


split = "-----------------------------------------------"
def main():
    welcome()
    secret_number = generate_secret_number()
    
    user_guess = guess_number()
    
    bulls, cows = score(user_guess, secret_number)
    print(f"{bulls} bulls, {cows} cows")
    print(split)


def welcome():
    text = """
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
    """
    print(text)
    

def generate_secret_number():
    numbers = list(set(range(10)))
    random.shuffle(numbers)
    if numbers[0] == 0:
        random.shuffle(numbers)
    secret_number = "".join(str(number) for number in numbers[:4])
    return secret_number


def guess_number():
    while True:
        user_guess = input("Enter a number: ")
        
        if len(user_guess) != 4:
            print("Please enter a 4-digit number.")
            continue
        elif len(set(user_guess)) != 4:
            print("Please enter an unique digits.")
            continue
        elif user_guess[0] == "0":
            print("Enter a number that doesn't start with 0.")
            continue
        elif not user_guess.isdigit():
            print("Please enter digits.")
            continue
        else:
            break

    return user_guess


def score(guess_number, secret_number):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess_number[i] == secret_number[i]:
            bulls += 1
        elif guess_number[i] in secret_number:
            cows += 1
    




if __name__ == "__main__":
    main()