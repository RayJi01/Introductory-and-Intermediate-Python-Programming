# Rui Ji, ruiji@usc.edu
# ITP 115, Spring 2021
# Lab 1
def main():
    print(" ___ ")
    print("|   |")
    print("|   |")
    print("|___|")

    print("You don't frighten us, English pig-dogs!\n"
          "Go and boil your bottoms, sons of a silly person!\n"
          "\t\t   -\"Monty Python and the Holy Grail\"")
    # Ask the user the month, date, and day of the week. Store each answer in a variable.
    userinputday = input("Enter the day of the week:")
    userinputmonth = input("Enter the month:")
    userinputdate = int(input("Enter the date:"))
    print("Today is ", userinputday, ", ", userinputmonth, " ", userinputdate,
          ". Tomorrow will be ", userinputmonth, " ", userinputdate + 1, ".", sep="")


# Make sure to convert the date to an integer. Print a message with today’s date and
# tomorrow’s date.


main()
