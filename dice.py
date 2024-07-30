import random

def dice():
    return random.randint(1,6)

while True:
    number_of_players = input("How many of you are playing (1-4)? (q to quit) ")
    if number_of_players == "q":
        quit()
    elif number_of_players.isdigit():
        number_of_players = int(number_of_players)
        if number_of_players < 1 or number_of_players > 4:
            print("Enter valid number.")
        else:
            break
    else:
        print("Please follow up the instructions...")

max_score = 49
scores = [0 for player in range(number_of_players)]


for player in range(number_of_players):
    current_score = 0
    print(f"Player nr.{player+1} is rolling...")

    while current_score <= max_score:
        roll = input("Roll the dice (y/n): ").lower()
        if roll not in ["y","n"]:
            print("Enter valid answer!")
            continue
        else:
            if roll == "y":
                value = dice()
                current_score += value
                print(f"You got {value}. Current score is {current_score}")
                if value == 1:
                    current_score = 0
                    print("Game over...")
                    break
            else:
                print(f"Your final score is {current_score}!")
                break
        scores[player] = current_score

print("\nFinal results:")
for player,score in enumerate(scores):
    print(f"Player {player+1} : {score} pts")
