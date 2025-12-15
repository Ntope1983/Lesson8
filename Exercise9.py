#Simple Game "scissors", "rock", "paper"
import random

objects = ["scissors", "rock", "paper"]


def input_integer(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Give a Integer please.")


total_win_player = 0
total_win_computer = 0
round_game = 1
while total_win_player < 3 and total_win_computer < 3:
    choice_number = input_integer("Input  a choice 1:scissors  2:rock  3:paper")
    while choice_number not in {1, 2, 3}:
        choice_number = input_integer("Input  again a choice 1:scissors  2:rock  3:paper")
    choice_gamer = objects[choice_number - 1]
    choice_computer = random.choice(objects)
    if choice_gamer == choice_computer:
        print("DRAW")
    elif choice_gamer == "rock" and choice_computer == "scissors":
        print("You Win")
        total_win_player += 1
    elif choice_gamer == "scissors" and choice_computer == "paper":
        print("You Win")
        total_win_player += 1
    elif choice_gamer == "paper" and choice_computer == "rock":
        print("You Win")
        total_win_player += 1
    else:
        print("You lost")
        total_win_computer += 1
    print(f"ROUND:{round_game} Wins Gamer:{total_win_player} Wins Computer: {total_win_computer}")
    round_game += 1
