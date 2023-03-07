# Rui Ji, ruiji@usc.edu
# ITP 115, Spring 2021
# Lab 8
from random import choice


def coin():
    p = choice(range(2))
    return p     # we determine that when return 0, its head. And when return 1, its tail.


def experiment():
    count = 0
    count_head = 0
    while count_head < 3:
        a = coin()
        if a == 0:
            count += 1
            count_head += 1
        else:
            count += 1

    return count


def main():
    total_games = 0
    total_times = 0
    while total_games < 10:
        single_times = experiment()
        total_games += 1
        total_times = total_times + single_times

    Average_times = total_times/10
    print("The average for 3 heads in a row is: " + str(Average_times))

main()



