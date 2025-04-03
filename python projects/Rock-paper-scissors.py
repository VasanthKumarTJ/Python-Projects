import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_num = random.randint(0,2)
    computer_choice = options[random_num]
    
    if user_input == "rock" and computer_choice == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_choice == "scissors":
        print("Tie!")
    elif user_input == "paper" and computer_choice == "paper":
        print("Tie!")
    elif user_input == "rock" and computer_choice == "rock":
        print("Tie!")
    else:
        print("You lost!")
        computer_wins += 1

    print(f"You picked {user_input.upper()}, Computer picked  {computer_choice.upper()}")
    print("You won", user_wins, "times")
    print("The   won", computer_wins, "times")
print("Goodbye!")