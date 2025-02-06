import random

EASY_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 10

def check_number(guess,number):
    """Check answer of the user"""
    if guess == number:
        print(f"You got it! The answer was {number}")
        return True
    elif guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")

    return False

def set_difficulty():
    """Set difficulty of the Game"""
    difficulty = input("Choose the level of difficulty. Type 'easy' or 'hard': ")
    lives = HARD_LEVEL_TURNS if difficulty == 'easy' else EASY_LEVEL_TURNS
    return lives

def guessing_game():
    print('Welcome to the Number Guessing Game!')
    number = random.randint(1, 100)
    lives = set_difficulty()

    while range(lives):
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if check_number(guess, number):
            break

        lives -= 1
        if lives > 0:
            print("Guess again.")
        else:
            print(f"You have run out of lives. the number was {number} :(")


guessing_game()