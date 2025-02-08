import random
import game_data
from art import logo, vs

print(logo)
random_a = random.choice(game_data.data)
random_b = random.choice(game_data.data)
game_over = False
score = 0


def format_data(data):
    return f"{data['name']}, {data['description']}, from {data['country']}"


while not game_over:
    # Print Data
    print(f"Compare A: {format_data(random_a)}")
    print(vs)
    print(f"Against B: {format_data(random_a)}")

    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Check Answer
    if user_answer == 'a' and random_a['follower_count'] > random_b['follower_count']:
        print("Correct")
        score += 1
        random_b = random.choice(game_data.data)
    elif user_answer == 'b' and random_b['follower_count'] > random_a['follower_count']:
        print("Correct")
        score += 1
        random_a = random_b
        random_b = random.choice(game_data.data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
