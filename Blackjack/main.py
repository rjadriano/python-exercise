import random
import art

def get_card():
    """Return Random card"""
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    return random.choice(cards)

def compute_score(hand):
    """Compute Hand Count"""
    total = 0
    for card in hand:
        if card in ['J','Q','K']:
            total += 10
        elif card == 'A':
            total += 11
        else:
            total += card

    if total > 21 and 'A' in hand:
        total = total - 10

    return total

def compare_score(player_score,computer_score):
    if 21 >= player_score > computer_score or computer_score > 21:
        return "You Win! :D"
    elif player_score == computer_score:
        return "Draw :|"
    else:
        return "You Lose :'("

def blackjack():
    print(art.logo)
    player_hand = []
    computer_hand = []
    player_score = 0
    computer_score = 0
    player_draw = 'y'
    # Deal Cards
    for x in range(2):
        player_hand.append(get_card())
        computer_hand.append(get_card())
    # Initial Hand
    while player_draw == 'y':
        player_score = compute_score(player_hand)
        computer_score = compute_score(computer_hand)

        if player_score >= 21:
            break

        print(f"Your cards: {", ".join(map(str, player_hand))} , current score {player_score}")
        print(f"Computer's first card: {computer_hand[0]} , current score {compute_score([computer_hand[0]])}")

        player_draw = input("Type 'y' to Draw another card, Type 'n' to pass: \n")
        if player_draw == 'y':
            player_hand.append(get_card())

    # Final Results
    while computer_score < 17 and player_score < 22:
        computer_hand.append(get_card())
        computer_score = compute_score(computer_hand)

    print(f"\nYour Final hand : {", ".join(map(str, player_hand))} , current score {player_score}")
    print(f"Computer's Final hand : {", ".join(map(str, computer_hand))} , current score {computer_score}")

    print(compare_score(player_score, computer_score))
    return

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print('\n' * 100)
    blackjack()
