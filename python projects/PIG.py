import random

def roll():
    min_num = 2
    max_num = 6
    roll = random.randint(min_num, max_num)
    return roll

while True:
    player = input("Enter num of players ( 2- 4 or Q to quit): ")
    if player == "q":
        break
    if player.isdigit():
        player = int(player)
        if player in range(2, 5):
           break
        else:
            print("Must be between 2 - 4")
            continue
    else:
        print("Please enter a valid number")
        continue

max_score = 50
players_scores = [0 for _ in range(player)]

while max(players_scores) < max_score:

    for player_idx in range(player):
        print(f"\nPlayer {player_idx + 1}'s turn\n")
        print("Your current score is: ", players_scores[player_idx], "\n")

        current_score = 0
        while True:
            should_roll = input("Do you want to roll? (Y/N): ").lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}. Current score: {current_score}")
        players_scores[player_idx] += current_score    
        print("your total score is: ", players_scores[player_idx])

max_score = max(players_scores)
winner = players_scores.index(max_score) + 1    
print(f"\nPlayer {winner} wins with a score of {max_score}!")
print("Goodbye!")