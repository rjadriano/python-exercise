import random

def number_check(number_order):
       while True:
           try:
                return int(input(f'Give the {number_order} number: '))
           except ValueError:
               print('Enter Valid Number')

first_intl = number_check('first')
second_intl = number_check('second')

# Fixed order of Range
if first_intl < second_intl:
    first, second = first_intl ,second_intl
else:
    second, first = first_intl, second_intl

guess_ctr = 1
mystery_number = random.randint(first,second)

while True:
    try:
        guess = int(input(f'Guess the number (between {first} and {second}): '))

        if guess == mystery_number:
            print('Congratulations! You guessed the number.')
            break
        elif guess_ctr == 3:
            print(f'Sorry you run out of attempts the number is {mystery_number}')
            break
        else:
            if guess < mystery_number:
                print('Too Low!')
            else:
                print('Too High!')
            guess_ctr += 1
    except ValueError:
        print('Enter Valid Number')