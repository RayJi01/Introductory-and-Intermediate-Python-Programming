# Rui Ji, ruiji@usc.edu
# ITP 115, Spring 2021
# Assignment 7
# Description:
# Describe what this program does.
from random import choice


def displayMenu():
    print("Welcome! Let's play rock, paper, scissors.")
    print("The rules of the game are: ")
    print("   Rock smashes scissors ")
    print("   Scissors cut paper")
    print("   Paper covers rock")
    print("   If both the choices are the same, it's a tie")
    return


def getComputerChoice():
    computer = choice(range(2))  # Determine the signatures that the computer will offered.
    return computer


def getPlayerChoice():
    player = ''
    print("Please choose (0) for rock, (1) for paper or (2) for scissors")
    while player not in range(3):
        player = int(input("> "))  # Ask the user to input again and again until they reach the 0,1,2

    return player


def playRound(a, b):
    if a < b:
        if a + 1 < b:
            return -1
        return 1
    if a > b:
        if a > b + 1:
            return 1
        return -1
    else:
        return 0


def continueGame():
    bool_value = ''
    while bool_value != "y" and bool_value != "n":
        bool_value = input("Do you want to continue playing (y or n)? ").lower()

    if bool_value == "y":
        return True
    return False


def main():
    quit_code = True

    ties = 0  # variable that count the number of games they tied.
    wins_c = 0
    wins_p = 0  # Two variable that store the number of game players and computers have won respectively.

    while quit_code:
        displayMenu()  # The intro of our game

        c_choice = getComputerChoice()

        p_choice = getPlayerChoice()

        game_result = playRound(c_choice, p_choice)

        if c_choice == 0:
            c_choice = "Rock"
        elif c_choice == 1:
            c_choice = "Paper"
        else:
            c_choice = "Scissors"  # define the meaning of the computer choice

        if p_choice == 0:
            p_choice = "Rock"
        elif p_choice == 1:
            p_choice = "Paper"
        else:
            p_choice = "Scissors"  # define the meaning of the player choice

        print("You chose " + str(p_choice))
        print("Computer chose " + str(c_choice))

        s = " cut "
        r = " smashes "  # Offer proper verbs to each results
        p = " covers "

        if game_result == -1:
            wins_c += 1
            if c_choice == "Scissors":
                print(c_choice + s + p_choice + ". Computer wins!")
            elif c_choice == "Rock":
                print(c_choice + r + p_choice + ". Computer wins!")
            elif c_choice == "Paper":
                print(c_choice + p + p_choice + ". Computer wins!")
        elif game_result == 0:
            ties += 1
            print("You tied with the computer")
        else:
            wins_p += 1
            if p_choice == "Scissors":
                print(p_choice + s + c_choice + ". You win!")
            elif p_choice == "Rock":
                print(p_choice + r + c_choice + ". You win!")
            elif p_choice == "Paper":
                print(p_choice + p + c_choice + ". You win!")

        quit_code = continueGame()

    print("You won " + str(wins_p) + " game(s).")
    print("Computer won " + str(wins_c) + " game(s).")
    print("You tied with the computer " + str(ties) + " game(s)")
    print('\n' + "Thanks for playing!")


main()
