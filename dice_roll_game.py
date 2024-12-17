import random

counter = 0

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        try:
            number_of_dice = int(input('How many dice : '))
            result = []
            for num in range(number_of_dice):
                result.append(random.randint(1, 6))

            print(result)
            counter += 1
        except ValueError:
            print('Enter Valid Number!')
    elif choice == 'n':
        print(f'You rolled {counter} time(s)!')
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')