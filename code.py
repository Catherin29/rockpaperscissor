import random

choices = ["rock", "paper", "scissor"]


def main():
    while True:
        computer = random.choice(choices)
        player = input("Enter any from this {} :".format(choices))
        player = player.lower()
        while player not in choices:
            player = input("Enter any from this {} :".format(choices))
        print("computer: ", computer)
        print("player: ", player)
        if player == computer:
            print("Match tie")
            return 0
        if player == 'rock':
            if computer == 'paper':
                print("Computer wins !")
                return 0
            if computer == 'scissor':
                print("Player wins !")
                return 1
        if player == 'paper':
            if computer == 'rock':
                print("Player wins !")
                return 1
            if computer == 'scissor':
                print("Computer wins !")
                return 0
        if player == 'scissor':
            if computer == 'rock':
                print("Computer wins !")
                return 0
            if computer == 'paper':
                print("Player wins !")
                return 1
        print("--------------------")


main()
choose = ("yes", "no")
while True:
 again = input("Do you want to play again(yes/no): ").lower()
 while again not in choose:
     again = input("Do you want to play again(yes/no): ").lower()
 if again == 'yes':
     main()
 else:
     print("bye bye")
     break