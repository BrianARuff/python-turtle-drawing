import random

wins = 0
ties = 0
losses = 0
print("Welcome to Rock, Paper, Scissors")
print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

computer = random.randint(1, 3)
user = input("1. Rock, 2. Paper, 3. Scissors, 9. Quit")

while user != 9:
    if wins == 3 or ties == 3 or losses == 3:
        break
    if user == 1 and computer == 1:
        print("Tie")
        ties += 1
    elif user == 1 and computer == 2:
        print("Computer")
        losses += 1
    elif user == 1 and computer == 1:
        print("Human")
        wins += 1
    elif user == 2 and computer == 2:
        print("Tie")
        ties += 1
    elif user == 2 and computer == 1:
        print("Human")
        wins += 1
    elif user == 2 and computer == 3:
        print("Computer")
        losses += 1
    elif user == 3 and computer == 3:
        print("Tie")
        ties += 1
    elif user == 3 and computer == 1:
        print("Computer")
        losses += 1
    else:
        print("Human")
        wins += 1

print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))