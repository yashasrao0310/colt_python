#case1: import random
# random.randint(0,2) OR case2: below implemented
from random import randint

print('rock...')
print('paper...')
print('scissors...')
computer = randint(0,2)      # 0-2 inclusive
if computer == 1:
    computer = 'rock'
elif computer == 2:
    computer = 'paper'
else:
    computer = 'scissors'
    
player = input("Enter your choice: ").lower()
print("Computer plays: " + computer)

if player == computer:
    print("It's a tie!")
elif player == 'rock':
    if computer == 'paper':
        print("computer wins!")
    else:
        print("player wins!")
elif player == 'paper':
    if computer == 'rock':
        print("player wins!")
    else:
        print("computer wins!")
elif player == 'scissors':
    if computer == 'paper':
        print("player wins!")
    else:
        print("computer wins!")
else:
    print("Please enter a valid move!")
