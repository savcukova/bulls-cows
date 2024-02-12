import random


#main function
def main():
    split = "-----------------------------------------------"
    welcome_text()
    secret_number = generate_secret_number()
    print(secret_number)
    
    attemps = 0
    while True:
        user_guess = guess_number()
        attemps += 1
    
        bulls, cows = score(user_guess, secret_number)
        print(f"{bulls} bulls, {cows} cows")
        print(split)
        if bulls == 4:
            print(f"Correct, you've guessed the right number in {attemps} guesses!")
            print(f"That's {rating(attemps)}")
            print(split)
            break
    
#welcome text
def welcome_text() -> None:
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
 
#secret number
def generate_secret_number() -> int:
    numbers = list(set(range(10)))
    random.shuffle(numbers)
    if numbers[0] == 0:
        random.shuffle(numbers)
    secret_number = "".join(str(number) for number in numbers[:4])
    return secret_number
        
# guess number 
def guess_number() -> int:
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
        

#VYHODNOTIT TIP UZIVATELE
def score(guess_number, secret_number):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess_number[i] == secret_number[i]:
            bulls += 1
        elif guess_number[i] in secret_number:
            cows += 1
        elif guess_number == secret_number:
            print("Correct, you've guessed the right number in ... guesses!")
    return bulls, cows


def rating(attemps):
    if attemps == 1:
        return "amazing"
    elif attemps <= 4:
        return "good"
    elif attemps <= 10:
        return "average"
    else:
        return "not so good"


if __name__ == "__main__":
    main()
