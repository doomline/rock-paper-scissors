from random import randint

#create a list housing the options available
throw = ["rock", "paper", "scissor"]

# create the computer opponent who has access to the options
computer = throw[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("you lose!")
        else:
            print("You win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("you lose!")
        else:
            print("You win!")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!")
        else:
            print("You win")
    else:
        print("Your spelling is off, I can't read that")

    player = False
    computer = throw[randint(0,2)]