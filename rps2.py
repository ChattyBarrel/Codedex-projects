import random 


print("====================")
print("Rock Paper Scissors")
print("====================")


print("1) rock")
print("2) paper")
print("3) scissors")

player = int(input("Pick a number: "))
comp = random.randint(1, 3)

if player == 1:
    player_choice = "Rock"
elif player == 2:
    player_choice = "Paper"
elif player == 3:
    player_choice = "Scissors"
print(f"You chose {player_choice}")

if comp == 1:
    comp_choice = "Rock"
elif comp == 2:
    comp_choice = "Paper"
elif comp == 3:
    comp_choice = "Scissors"
print(f"Computer chose {comp_choice}")

if comp == player:
    print("It's a tie!")
elif (comp == 1 and player == 3) or (comp == 2 and player == 1) or (comp == 3 and player == 2):
    print("You lost :(")
elif (comp == 1 and player == 2) or (comp == 2 and player == 3) or (comp == 3 and player == 1):
    print("You Win!!")



















