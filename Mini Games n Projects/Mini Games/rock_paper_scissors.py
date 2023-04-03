import random

user_wins = 0
computer_wins = 0
tie = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/ Paper/ Scissors or Q to quit the game: ").lower()
    if user_input == "q":
        break

    # put user's input in a list with two brackets
    if user_input not in options:
        # user has to re-input the value
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1 and scissors = 2
    computer_move = options[random_number]
    print(f"Computer's move: {computer_move}")

    if user_input == "rock" and computer_move == "scissors" \
            or user_input == "paper" and computer_move == "rock" \
            or user_input == "scissors" and computer_move == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_move:
        print("It was a tie!")
        tie += 1
    else:
        print("You lost!")
        computer_wins += 1

print(f"You won {int(user_wins)} times.")
print(f"Computer won {int(computer_wins)} times.")
print(f"The tie came up with {int(tie)} times.")
print("Thanks for playing :)")
