# Rui Ji, ruiji@usc.edu
# ITP 115, Spring 2021
# Lab 7

def printRect(length, width):
    k = int(length)
    b = int(width)
    print(' ' + "-" * b + ' ')
    print(("|" + ' ' * b + "|" + '\n') * (k-1) + "|" + ' ' * b + "|")
    print(' ' + "-" * b + ' ')


def printSquare(size):
    l = int(size)
    print(' ' + "-" * l + ' ')
    print(("|" + ' ' * l + "|" + '\n') * (l-1) + "|" + ' ' * l + "|")
    print(' ' + "-" * l + ' ')


def main():
    print("Welcome to the Shape Printer!")
    print("R) Rectangle")
    print("S) Square")
    game_mode = input("Enter the shape you want to print: ").lower()
    if game_mode == "r":
        user_len = input("Enter the length: ")
        user_width = input("Enter the width: ")
        print(printRect(user_len, user_width))
    elif game_mode == "s":
        user_size = input("Enter the size:")
        print(printSquare(user_size))

main()