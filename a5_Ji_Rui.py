# Rui Ji, ruiji@usc.edu
# ITP 115, Spring 2021
# Assignment 5
# Description: Part I and Part II are in the same file. Part II started at around line 303
# Describe what this program does:

# Part 1: Create a alphabet counting programme
def main():
    # Store the user input sentence into a list so that we can count for elements inside the list later.
    list_sentence = []
    sentence = input("Please enter a sentence: ")
    # To avoid the "space" to be counted as special characters, we need to remove all the "spaces" in our input list.
    sentence1 = sentence.replace(" ", "")
    list_sentence = sentence1
    # In order to count the times of appearance of each number, we need 26 lists to store each of their chances of
    # appearances.
    num_special = 0
    list_special = []
    num_a = 0
    list_a = []
    num_b = 0
    list_b = []
    num_c = 0
    list_c = []
    num_d = 0
    list_d = []
    num_e = 0
    list_e = []
    num_f = 0
    list_f = []
    num_g = 0
    list_g = []
    num_h = 0
    list_h = []
    num_i = 0
    list_i = []
    num_j = 0
    list_j = []
    num_k = 0
    list_k = []
    num_l = 0
    list_l = []
    num_m = 0
    list_m = []
    num_n = 0
    list_n = []
    num_o = 0
    list_o = []
    num_p = 0
    list_p = []
    num_q = 0
    list_q = []
    num_r = 0
    list_r = []
    num_s = 0
    list_s = []
    num_t = 0
    list_t = []
    num_u = 0
    list_u = []
    num_v = 0
    list_v = []
    num_w = 0
    list_w = []
    num_x = 0
    list_x = []
    num_y = 0
    list_y = []
    num_z = 0
    list_z = []
    # Search for each letter in the list
    for i in list_sentence:
        if i == "a" or i == "A":
            num_a = num_a + 1
            total_a = num_a
            list_a.append(total_a)
        elif i == "b" or i == "B":
            num_b = num_b + 1
            total_b = num_b
            list_b.append(total_b)
        elif i == "c" or i == "C":
            num_c = num_c + 1
            total_c = num_c
            list_c.append(total_c)
        elif i == "d" or i == "D":
            num_d = num_d + 1
            total_d = num_d
            list_d.append(total_d)
        elif i == "e" or i == "E":
            num_e = num_e + 1
            total_e = num_e
            list_e.append(total_e)
        elif i == "f" or i == "F":
            num_f = num_f + 1
            total_f = num_e
            list_f.append(total_f)
        elif i == "g" or i == "G":
            num_g = num_g + 1
            total_g = num_g
            list_g.append(total_g)
        elif i == "h" or i == "H":
            num_h = num_h + 1
            total_h = num_e
            list_h.append(total_h)
        elif i == "i" or i == "I":
            num_i = num_i + 1
            total_i = num_e
            list_i.append(total_i)
        elif i == "j" or i == "J":
            num_j = num_j + 1
            total_j = num_j
            list_j.append(total_j)
        elif i == "k" or i == "K":
            num_k = num_k + 1
            total_k = num_k
            list_k.append(total_k)
        elif i == "l" or i == "L":
            num_l = num_l + 1
            total_l = num_l
            list_l.append(total_l)
        elif i == "m" or i == "M":
            num_m = num_m + 1
            total_m = num_m
            list_m.append(total_m)
        elif i == "n" or i == "N":
            num_n = num_n + 1
            total_n = num_n
            list_n.append(total_n)
        elif i == "o" or i == "O":
            num_o = num_o + 1
            total_o = num_e
            list_o.append(total_o)
        elif i == "p" or i == "P":
            num_p = num_p + 1
            total_p = num_p
            list_p.append(total_p)
        elif i == "q" or i == "Q":
            num_q = num_q + 1
            total_q = num_q
            list_q.append(total_q)
        elif i == "r" or i == "R":
            num_r = num_r + 1
            total_r = num_r
            list_r.append(total_r)
        elif i == "s" or i == "S":
            num_s = num_s + 1
            total_s = num_s
            list_s.append(total_s)
        elif i == "t" or i == "T":
            num_t = num_t + 1
            total_t = num_t
            list_t.append(total_t)
        elif i == "u" or i == "U":
            num_u = num_u + 1
            total_u = num_u
            list_u.append(total_u)
        elif i == "v" or i == "V":
            num_v = num_v + 1
            total_v = num_v
            list_v.append(total_v)
        elif i == "w" or i == "W":
            num_w = num_w + 1
            total_w = num_w
            list_w.append(total_w)
        elif i == "x" or i == "X":
            num_x = num_x + 1
            total_x = num_x
            list_x.append(total_x)
        elif i == "y" or i == "Y":
            num_y = num_y + 1
            total_y = num_y
            list_y.append(total_y)
        elif i == "z" or i == "Z":
            num_z = num_z + 1
            total_z = num_z
            list_z.append(total_z)
        else:
            num_special = num_special + 1
            total_special = num_special
            list_special.append(total_special)
    # If the letter appear once, they will be one value appear in our list, we can finally print the length
    # of list to count how many time the number appear.
    print("Here is the character distribution: ")
    print('\n')
    if len(list_special) != 0:
        print("special characters: " + "*" * len(list_special))
    else:
        print("special characters: None")
    # If the characters never appear, we manually print none to these cases.
    if len(list_a) != 0:
        print("a: " + "*" * len(list_a))
    else:
        print("a: None")
    if len(list_b) != 0:
        print("b: " + "*" * len(list_b))
    else:
        print("b: None")
    if len(list_c) != 0:
        print("c: " + "*" * len(list_c))
    else:
        print("c: None")
    if len(list_d) != 0:
        print("d: " + "*" * len(list_d))
    else:
        print("d: None")
    if len(list_e) != 0:
        print("e: " + "*" * len(list_e))
    else:
        print("e: None")
    if len(list_f) != 0:
        print("f: " + "*" * len(list_f))
    else:
        print("f: None")
    if len(list_g) != 0:
        print("g: " + "*" * len(list_g))
    else:
        print("g: None")
    if len(list_h) != 0:
        print("h: " + "*" * len(list_h))
    else:
        print("h: None")
    if len(list_i) != 0:
        print("i: " + "*" * len(list_i))
    else:
        print("i: None")
    if len(list_j) != 0:
        print("j: " + "*" * len(list_j))
    else:
        print("j: None")
    if len(list_k) != 0:
        print("k: " + "*" * len(list_k))
    else:
        print("k: None")
    if len(list_l) != 0:
        print("l: " + "*" * len(list_l))
    else:
        print("l: None")
    if len(list_m) != 0:
        print("m: " + "*" * len(list_m))
    else:
        print("m: None")
    if len(list_n) != 0:
        print("n: " + "*" * len(list_n))
    else:
        print("n: None")
    if len(list_o) != 0:
        print("o: " + "*" * len(list_o))
    else:
        print("o: None")
    if len(list_p) != 0:
        print("p: " + "*" * len(list_p))
    else:
        print("p: None")
    if len(list_q) != 0:
        print("q: " + "*" * len(list_q))
    else:
        print("q: None")
    if len(list_r) != 0:
        print("r: " + "*" * len(list_r))
    else:
        print("r: None")
    if len(list_s) != 0:
        print("s: " + "*" * len(list_s))
    else:
        print("s: None")
    if len(list_t) != 0:
        print("t: " + "*" * len(list_t))
    else:
        print("t: None")
    if len(list_u) != 0:
        print("u: " + "*" * len(list_u))
    else:
        print("u: None")
    if len(list_v) != 0:
        print("v: " + "*" * len(list_v))
    else:
        print("v: None")
    if len(list_w) != 0:
        print("w: " + "*" * len(list_w))
    else:
        print("w: None")
    if len(list_x) != 0:
        print("x: " + "*" * len(list_x))
    else:
        print("x: None")
    if len(list_y) != 0:
        print("y: " + "*" * len(list_y))
    else:
        print("y: None")
    if len(list_z) != 0:
        print("z: " + "*" * len(list_z))
    else:
        print("z: None")


main()




# Part II:

def main():
    list_case1 = []
    # A random function that enable us to randomly pick the "Case" we gonna play
    from random import choice
    # Create 5 list for each playing cases.
    list_case1 = list(range(2, 21, 2))
    list_case2 = list(range(1, 20, 2))
    list_case3 = list(range(5, 11))
    list_case4 = list(range(10, 21))
    list_case5 = list(range(3, 19, 3))
    list_play_case = [list_case1, list_case2, list_case3, list_case4, list_case5]
    # Create our dices:
    d = range(1, 21)
    dice = list(d)
    # Create our score counter:
    user_score = 0
    # Create a number to count the amounts of games we've play. And a list of length 11 to determine if we play 10 games
    times = 0
    t = range(0, 10)
    games = list(t)

    for times in games:
    #Randomly select case_list from the total play case, we first need to know which case we select.
        case_number = choice(range(4))
        dice_number = choice(dice)
        print("You are playing for CASE " + str(case_number+1))
        print("You will win for the following numbers: ")
    # Then select the corresponding list that we give the user to play.
        print(list_play_case[case_number])
        print('\n')
    # Every once we print out the rolling pages, count the times we've played at once.
        times += 1
        print("Now Rolling... ")
        print("You rolled a " + str(dice_number) + "!")
        if dice_number in list_play_case[case_number]:
            print("You won 50 points! :) ")
            # Give some spaces to the next turn.
            print('\n')
            user_score += 50
        else:
            print("You didn't win :( ")
            print('\n')

    print("Your total score is: " + str(user_score))
    print("Thanks for playing! ")





main()