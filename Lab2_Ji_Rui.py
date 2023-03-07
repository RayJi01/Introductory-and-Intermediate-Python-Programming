# Rui Ji, ruiji@usc.edu
# ITP 115, Summer 2021
# Lab 2

def main():
    size = input("What size coffee do you want (S, M, L)?")
    degrees = int(input("What temperature would you like (in degrees)?"))
    beansandblends = input("What type of beans / blend would you like?")
    creams = input("Would you like room for cream (y/n)?")

    if size == "S" or size == "s":
        coffeeSize = "small"
    elif size == "M" or size == "m":
        coffeeSize = "medium"
    else:
        coffeeSize = "Large"

    if degrees >= 90:
        coffeeTemp = "hot"
    else:
        coffeeTemp = "iced"

    if creams == "y" or creams == "Y":
        coffeeCreamModifier = "with creams"
    else:
        coffeeCreamModifier = "with no creams"

        print("You ordered a " + "" + coffeeSize + " " + coffeeTemp + "" + beansandblends + " " + coffeeCreamModifier)


main()
