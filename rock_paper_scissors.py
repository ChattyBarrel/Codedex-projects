import random


print("====================")
print("Rock Paper Scissors")
print("====================")

print("1) rock")
print("2) paper")
print("3) scissors")

player = input("Please select: ")
print(f"You chose: {player}")
comp = ["Rock", "Paper", "Scissors"]
comp_choices = random.choice(comp)
print(f"Computer chose: {comp_choices}")


if player == "rock" and comp == "Paper":
    print("You lose")
elif player == "paper" and comp == "Scissors":
    print("You lose")
elif player == "scissors" and comp == "Rock":
    print("You lose")
elif player == "rock" and comp == "Scissors":
    print("You Win!")
elif player == "paper" and comp == "Rock":
    print("You Win!")
elif player == "scissors" and comp == "Paper":
    print("You Win!")
elif player == "rock" and comp == "Rock":
    print("It's a tie")
elif player == "paper" and comp == "Paper":
    print("It's a tie")
elif player == "scissors" and comp == "Scissors":
    print("Its's a tie ")
else:
    print("Wrong input")

