# without score and play again 
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
