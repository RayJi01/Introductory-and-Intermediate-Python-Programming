# Rui Ji, ruiji@usc.edu
# ITP 115, Spring 2021
# Lab 3
def main():
    userinput = "not q"
    while userinput != "q":
        print("What would you like to know?")
        print("a) Favorite Animal")
        print("c) Favorite Color")
        print("m) Favorite Meal")
        print("q) Quit")

        userinput = input("> "). lower()

        if userinput == "a":
            print("My favorite animal is puppies!")
        elif userinput == "c":
            print("My favorite color is blue")
        elif userinput == "m":
            print("My favorite meal is in-n-out!")
        elif userinput == "q":
            print("Goodbye!")
        else:
            print("That option is not available. ")

    print()



main()