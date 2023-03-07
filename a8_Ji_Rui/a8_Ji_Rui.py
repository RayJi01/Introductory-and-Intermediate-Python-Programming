# Rui Ji, ruiji@usc.edu
# ITP 115, Summer 2021
# Assignment 8
# Description:
# Describe what this program does.


import TicTacToeHelper
from random import choice


def isValidMove(boardList, spot):
    if spot not in range(9):
        return False
    elif str(spot) not in boardList:
        return False
    return True


def updateBoard(boardList, spot, playerLetter):
    boardList[spot] = playerLetter
    return


def playGame():
    board_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    computer_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    move_counter = 0  # move_counter serve to calculate the total rounds in one game

    # Extra credit: allow the user to determine the role when they start.
    user_role = "player_choice"
    while user_role != "x" and user_role != "o":
        user_role = input("which player shall you pick? (1) X (2) O").lower()  # player_determined used to determine the who should start and who will win

    # Extra Credit: Let the user to determine if they want to play with the computer:
    player_choice = 'computer or not'
    while player_choice != "y" and player_choice != 'n':
        player_choice = input("Do you want to play against the computer? (y/n) ").lower()

    # play with the computer
    if player_choice == "y":
        game_check = TicTacToeHelper.checkForWinner(board_list, move_counter)
        if user_role == "x":
            while game_check == "n":
                print(move_counter)
                print(game_check)
                TicTacToeHelper.printUglyBoard(board_list)  # Print the updated board all the time before start
                if move_counter % 2 == 0:
                    # Player X will start while player_determined can be divide by 2 since it start with 0.
                    player_letter = "x"
                    player_input = int(input("Player x, pick a spot: "))
                    result = isValidMove(board_list, player_input)  # determine whether the player's choice is valid.
                    while result is False:
                        player_input = int(input("Invalid move, please try again." + '\n' + "Player x, pick a spot: "))
                        # ask him to re-input until he reach a valid choice
                    else:
                        updateBoard(board_list, player_input, player_letter)
                        computer_list.remove(str(player_input))
                        move_counter += 1
                        game_check = TicTacToeHelper.checkForWinner(board_list, move_counter)

                        # update the board after valid input and update the determintor for the game process
                else:
                    computer_letter = "o"  # repeat the whole section for player o
                    random = (choice(computer_list))   # computer should use a exclusive list for determination
                    player_input = int(random)
                    computer_list.remove(random)   # Remove the spots where we select.

                    updateBoard(board_list, player_input, computer_letter)
                    move_counter += 1
                    game_check = TicTacToeHelper.checkForWinner(board_list, move_counter)


            else:
                if game_check != "s":  # if there is a winner
                    if move_counter % 2 == 0:
                        # when the game_check perform instructions of endings, run certain procession
                        winner = "Player o"  # determine the winner
                    else:
                        winner = "Player x"
                    TicTacToeHelper.printUglyBoard(board_list)  # show the board when the game ends.
                    print("Game Over!")
                    print(winner + " is the winner!")
                else:  # if they reach the stalemate!
                    print(TicTacToeHelper.printUglyBoard(board_list))
                    print("Game Over!")
                    print("Stalemate reached!")
        else:
            while game_check == "n":
                TicTacToeHelper.printUglyBoard(board_list)  # Print the updated board all the time before start
                if move_counter % 2 == 1:
                    # Player X will start while player_determined can be divide by 2 since it start with 0.
                    player_letter = "o"
                    player_input = int(input("Player x, pick a spot: "))
                    result = isValidMove(board_list, player_input)  # determine whether the player's choice is valid.
                    while result is False:
                        player_input = int(input("Invalid move, please try again." + '\n' + "Player x, pick a spot: "))
                        # ask him to re-input until he reach a valid choice
                    else:
                        updateBoard(board_list, player_input, player_letter)
                        computer_list.remove(str(player_input))
                        move_counter += 1
                        game_check = TicTacToeHelper.checkForWinner(board_list, move_counter)

                        # update the board after valid input and update the determintor for the game process
                else:
                    computer_letter = "x"  # repeat the whole section for player o
                    random = (choice(computer_list))
                    player_input = int(random)
                    computer_list.remove(random)

                    updateBoard(board_list, player_input, computer_letter)
                    move_counter += 1
                    game_check = TicTacToeHelper.checkForWinner(board_list, move_counter)

            else:
                if game_check != "s":  # if there is a winner
                    if move_counter % 2 == 0:
                        # when the game_check perform instructions of endings, run certain procession
                        winner = "Player o"  # determine the winner
                    else:
                        winner = "Player x"
                    TicTacToeHelper.printUglyBoard(board_list)  # show the board when the game ends.
                    print("Game Over!")
                    print(winner + " is the winner!")
                else:  # if they reach the stalemate!
                    print(TicTacToeHelper.printUglyBoard(board_list))
                    print("Game Over!")
                    print("Stalemate reached!")

    else:  # Two player play against each other.
        game_check = TicTacToeHelper.checkForWinner(board_list, move_counter)
        while game_check == "n":
            TicTacToeHelper.printUglyBoard(board_list)  # Print the updated board all the time before start
            if move_counter % 2 == 0:
                # Player X will start while player_determined can be divide by 2 since it start with 0.
                player_letter = "x"
                player_input = int(input("Player x, pick a spot: "))
                result = isValidMove(board_list, player_input)  # determine whether the player's choice is valid.
                while result is False:
                    player_input = int(input("Invalid move, please try again." + '\n' + "Player x, pick a spot: "))
                    # ask him to re-input until he reach a valid choice
                else:
                    updateBoard(board_list, player_input, player_letter)
                    move_counter += 1
                    game_check = TicTacToeHelper.checkForWinner(board_list, move_counter)
                     # update the board after valid input and update the determintor for the game process
            else:
                player_letter = "o"  # repeat the whole section for player o
                player_input = int(input("Player o, pick a spot: "))
                result = isValidMove(board_list, player_input)
                while result is False:
                    player_input = int(input("Invalid move, please try again." + '\n' + "Player o, pick a spot: "))
                else:
                    updateBoard(board_list, player_input, player_letter)
                    move_counter += 1
                    game_check = TicTacToeHelper.checkForWinner(board_list, move_counter)


        else:
            if game_check != "s":  # if there is a winner
                if move_counter % 2 == 0:
                    # when the game_check perform instructions of endings, run certain procession
                    winner = "Player o"  # determine the winner
                else:
                    winner = "Player x"
                TicTacToeHelper.printUglyBoard(board_list)  # show the board when the game ends.
                print("Game Over!")
                print(winner + " is the winner!")
            else:  # if they reach the stalemate!
                print(TicTacToeHelper.printUglyBoard(board_list))
                print("Game Over!")
                print("Stalemate reached!")


def main():
    print("Welcome to Tic Tac Toe!")
    playGame()
    userInput = input("Would you like to play another round? (y/n): ")
    while userInput == "y":
        playGame()
        userInput = input("Would you like to play another round? (y/n): ")
    print("GoodBye! ")


main()
