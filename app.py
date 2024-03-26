import random


def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players(1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Must be between 1 and 4")
    else:
        print("Invalid, try again")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        should_roll = input("Yould you like to roll dice again? (Y/N):")
        if should_roll.lower() != 'y':
            break

        value = roll_dice()
        if value == 1:
            print("You rolled a 1! Turn done")
        else:
            current_score += value



