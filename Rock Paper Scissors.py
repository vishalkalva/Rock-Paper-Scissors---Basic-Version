# Version 1 — Basic Game

import random

choice = ("rock", "paper" , "scissors")

user = input("enter rock, paper, scissors:")

computer = random.choice(choice)

print ("you choice:" ,user)
print ("computer choice:" ,computer)

if user == computer :
    print("it's a tie")

elif (user == "rock" and computer == "scissors") or\
    (user == "paper" and computer == "rock")or\
    (user == "scissors" and computer == "paper"):
    print("you won!")

else:
    print("computer won!")



# Version 2 — Score & Replay

import random

choice = ("rock", "paper", "scissors")

user_score = 0
computer_score = 0

while True:

    user = input("Enter rock, paper, scissors: ").lower()

    computer = random.choice(choice)

    print("Your choice:", user)
    print("Computer choice:", computer)

    if user == computer:
        print("It's a tie")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You won!")
        user_score += 1

    else:
        print("Computer won!")
        computer_score += 1

    print("Score - You:", user_score, "| Computer:", computer_score)

    again = input("Play again? (yes/no): ").lower()

    if again == "no":
        print("Final Score - You:", user_score, "| Computer:", computer_score)
        print("Thanks for playing!")
        break
