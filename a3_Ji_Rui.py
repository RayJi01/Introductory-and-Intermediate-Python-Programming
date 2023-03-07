# Rui Ji, ruiji@usc.edu
# ITP 115, Spring 2021
# Assignment 3
# Description:
# This program creates a Harry Potter vending machine.
# It determines change and gives a discount.

def main():
    print("Please select an item from the vending machine:")
    print("a) Butterbeer: 58 knuts")
    print("b) Quill: 10 knuts")
    print("c) The Daily Prophet: 7 knuts")
    print("d) Book of Spells: 400 knuts")

    userInput = input("> ")
    userinput2 = input("Will you share this on Instagram (y/n)? ")
    userinput3 = int(input("how many knuts you gonna pay?")) # the customers can enter how many knuts they gonna pay.
                                                             # for extra credit.

    if userInput == "a":
        # use the lowercase mode to generalize both the upper and lowercases.
        print("Will you share this on Instagram (y/n)? ")
        if userinput2.lower() == "y":
            print("You bought a Butterbeer for 58 knuts (with coupon of 5 knuts) and paid with" + str(userinput3) +
                  "knuts.")
            change = str(userinput3-int(58) + int(5))
            changeinsickles = str((userinput3-58+5)//29)
            changeinknuts = str((userinput3-58+5) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)
        # use the lowercase mode to generalize both the upper and lowercases.
        elif userinput2.lower() == "n":
            print("You bought a Butterbeer for 58 knuts (with coupon of 0 knuts) and paid with" + str(userinput3) +
                  "knuts.")
            change = str(userinput3-58)
            changeinsickles = str((userinput3-int(58))//29)
            changeinknuts = str((userinput3-int(58)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)
        # For anyone who didn't respond the coupon question correctly.
        else:
            print("You have entered an invalid option. No coupon will be used.")
            change = str(userinput3 - 58)
            changeinsickles = str((userinput3 - int(58)) // 29)
            changeinknuts = str((userinput3 - int(58)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)

    # Option B: buy a Quill which cost 10 knuts.
    if userInput == "b":
        print("Will you share this on Instagram (y/n)? ")
        if userinput2.lower() == "y":
            change = str(userinput3 - int(10) + int(5))
            changeinsickles = str((userinput3 - int(10) + int(5)) // 29)
            changeinknuts = str((userinput3 - int(10) + int(5)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)
        elif userinput2. lower() == "n":
            print("You bought a Butterbeer for 58 knuts (with coupon of 0 knuts) and paid with one gallon")
            change = str(493 - 10)
            changeinsickles = str((userinput3 - int(10)) // 29)
            changeinknuts = str((userinput3 - int(10)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)
        else:
            print("You have entered an invalid option. No coupon will be used.")
            change = str(userinput3 - 10)
            changeinsickles = str((userinput3 - int(10)) // 29)
            changeinknuts = str((userinput3 - int(10)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)

    # Option C: buy a daily prophet for 7 knuts:
    if userInput == "c":
        print("Will you share this on Instagram (y/n)? ")
        if userinput2. lower() == "y":
            change = str(userinput3 - int(7) + int(5))
            changeinsickles = str((userinput3 - int(7) + int(5)) // 29)
            changeinknuts = str((userinput3 - int(7) + int(5)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)
        elif userinput2. lower() == "n":
            change = str(userinput3 - int(7))
            changeinsickles = str((userinput3 - int(7)) // 29)
            changeinknuts = str((userinput3 - int(7)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)
        else:
            print("You have entered an invalid option. No coupon will be used.")
            change = str(userinput3 - 7)
            changeinsickles = str((userinput3 - 7)//29)
            changeinknuts = str((userinput3 - 7) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)

    # Option D: buy a Book of Spells for 400 knuts:
    if userInput == "d":
        print("Will you share this on Instagram (y/n)? ")
        if userinput2. lower() == "y":
            change = str(userinput3 - int(400) + int(5))
            changeinsickles = str((userinput3 - int(400) + int(5)) // 29)
            changeinknuts = str((userinput3 - int(400) + int(5)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)
        elif userinput2. lower() == "n":
            change = str(userinput3 - int(400))
            changeinsickles = str((userinput3 - int(400)) // 29)
            changeinknuts = str((userinput3 - int(400)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)
        else:
            print("You have entered an invalid option. No coupon will be used.")
            change = str(userinput3 - 400)
            changeinsickles = str((userinput3 - int(400)) // 29)
            changeinknuts = str((userinput3 - int(400)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)

    #  For customers who didn't choose the valid options. We will randomly assign them option a.
    else:
        print("You have entered an invalid option. You will be given a Butterbeer for 58 knuts.")
        print("Will you share this on Instagram (y/n)? ")
        if userinput2.lower() == "y":
            print("You bought a Butterbeer for 58 knuts (with coupon of 5 knuts) and paid with one gallon")
            change = str(userinput3-int(58)+ int(5))
            changeinsickles = str((userinput3-int(58)+int(5))//29)
            changeinknuts = str((userinput3-int(58)+int(5))%29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)
        elif userinput2.lower() == "n":
            print("You bought a Butterbeer for 58 knuts (with coupon of 0 knuts) and paid with one gallon")
            change = str(userinput3-58)
            changeinsickles = str((userinput3-int(58))//29)
            changeinknuts = str((userinput3-int(58)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)
        else:
            print("You have entered an invalid option. No coupon will be used.")
            change = str(userinput3 - 58)
            changeinsickles = str((userinput3 - int(58)) // 29)
            changeinknuts = str((userinput3 - int(58)) % 29)
            print("Here is your changes(" + change + "knuts): ")
            print("sickles: " + changeinsickles)
            print("knuts: " + changeinknuts)

main()