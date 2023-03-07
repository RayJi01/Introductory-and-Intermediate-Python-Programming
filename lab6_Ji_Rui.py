# Rui Ji, ruiji@usc.edu
# ITP 115, Spring 2021
# Lab 6

def main():
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    userinput1 = input("Enter a word #1: ")
    userinput2 = input("Enter a word #2: ")
    for m in userinput1:
        list1.append(m)
    for n in userinput2:
        list2.append(n)

    for i in list1:
        if i == ' ':
            list1.remove(' ')
        else:
            list1 = list1
    for q in list2:
        if q == ' ':
            list2.remove(' ')
        else:
            list2 = list2

    if len(list1) == len(list2):
        for f in list1:
            if f in list2:
                print("The words are anagrams!")
            else:
                print("The words are NOT anagrams.")
    else:
        print("The words are NOT anagrams.")
    print()

    userinput3 = input("Enter a phrase: ")
    a = userinput3.lower()

    for c in a:
        list3.append(c)
        list4.append(c)
    for k in list3:
        if k == ' ':
            list3.remove(' ')
        else:
            list3 = list3
    for r in list4:
        if r == ' ':
            list4.remove(' ')
        else:
            list4 = list4
    list3.reverse()
    if list3 == list4:
        print("The phrase is a palindrome!")
    else:
        print("The phrase is NOT a palindrome.")


main()