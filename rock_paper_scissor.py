import random

user_win, computer_win = 0, 0
emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = tuple(emojis.keys())
print('First to Three ROCK PAPER SCISSOR!!')

def get_user_input():
    while True:
        user = input('Rock, Paper, or Scissors? (r/p/s): ').lower()
        if user in choices:
            print(f'You chose {emojis[user]}')
            return user
        else:
            print('Invalid Choice!')

def get_computer_output():
    computer = random.choice(choices)
    print(f'Computer chose {emojis[computer]}')
    return computer

while True:
    user_input = get_user_input()
    computer_output = get_computer_output()

    if user_input == computer_output:
        print('Its a Tie')
    elif (
            (user_input == 'r' and computer_output == 's') or
            (user_input == 's' and computer_output == 'p') or
            (user_input == 'p' and computer_output == 'r')):
        print('You wind the Round')
        user_win += 1
    else:
        print('You Lose the Round')
        computer_win += 1

    print(f'You: {user_win} , Computer : {computer_win}')

    if user_win == 3 or computer_win == 3:
        if user_win > computer_win:
            print('Congratulations You Win 🔥')
        else:
            print('Better Luck Next Time 💩')
        should_continue = input('Rematch? (y/n)').lower()
        if should_continue == 'n':
            break
        else:
            user_win, computer_win = 0, 0