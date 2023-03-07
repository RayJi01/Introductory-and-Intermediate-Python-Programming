# Rui Ji, ruiji@usc.edu
# ITP 115, Summer 2021
# Assignment 2
# Description:
# Describe what this program does such as:
# This program creates a Mad Libs story.
# It gets input from the user and prints output.


def main():
    animals = input("Enter an animal (plural):")
    adjective = input("Enter an adjective:")
    adjective2 = input("Enter another adjective:")
    verb1 = input("Enter a verb:")
    verb2 = input("Enter a verb ending in 'ing':")
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a second number:"))
    num3 = int(input("Enter a third number:"))
    num4 = num1 + num2
    decimal = float(input("Enter a number with a decimal:"))

    print(
        "Today I adopted " + "\"" + str(num1) + "\"" + " pet " + "\"" + animals + "\"" +
        ". I learned that each animal needs " + "\"" + str(decimal) + "\"" + " hours of " + verb2 +
        " everyday, and that they travel in groups of " +
        str(num3) + ". They are so " + "\"" + adjective + "\"" + " that I decided to adopt " + "\"" + str(num2) +
        "\"" + " more. Now I have " + "\"" + str(num4) + "\" " + "\"" + animals + "\"" + " and I am so " + "\"" +
        adjective2 + "\"" + " that I want to " + "\"" + verb1 + "\"" + ".")


main()
