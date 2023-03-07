# Rui ji, ruiji@usc.edu
# ITP 115, Spring 2021
# Assignment 4
# Description: Use the while loops to create a mean computer program and select the max and min number
# Describe what this program does.
import pandas as pd


def main():
    num1 = "not -1"
    min = -1
    userinput2 = "not y"
    max = min
    user_list = []  # create a list to store all the inputs the user have ever entered.
    while userinput2.lower() != "n" or userinput2.lower() != "q":
        # loops will always run until the user plug in n or q, which turn to our next questions
        print("Input an integer greater than or equal to 0 (-1 to quit)")
        num1 = input("> ")
        while num1 != "-1":
            num1 = input("> ")
            user_list.append(int(num1))  # store every new inputs
            # determine if we need to change our min

            if min < int(num1):
                min = min
            else:
                min = int(num1)
            # determine if we need to change our max
            if max > int(num1):
                max = max
            else:
                max = int(num1)
        else:
            print("The largest number is " + str(max))
            print("The smallest number is " + str(min))
            print("The average number is " + str(sum(user_list) / len(user_list)))  # the sum of all inputs divide by
            # the number of inputs inside the list.
            userinput2 = input("Would you like to enter another set of numbers (y/n)?")
            if userinput2.lower() == "n" or userinput2.lower() == "q":
                # After asking for our user's answers, they choose n or q, we break the loops
                break
            else:
                max = min
                min = -1
                user_list = []
                # Otherwise, we will restart the loops and ask them to input value that we can continue to store as num1

    print("Goodbye!")


    list1 = ['1', ' 2', '3', '4', '5']
    print(list1[2])

main()
