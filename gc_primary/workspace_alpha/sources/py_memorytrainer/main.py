import numpy as np
import random
from time import sleep
import os
from __init__ import *


def clearscreen():
    # print('\x1b[2J\x1b[1;1H')
    os.system('cls')


def randnum(x):
    return random.randint(x, x + 10)


def randmemo(x):
    tup = []
    num = randnum(x)
    for i in range(num):
        tup.append(random.randint(0, 9))

    return np.array(tup)


def compare(x):
    clearscreen()
    memo = randmemo(x)
    print(memo)
    checklen = False
    sleep(1)
    print(f'{(x+1)*3}s\nMemorizing...', end='')
    sleep((x+1)*3)
    clearscreen()
    while checklen == False:
        result = input('Your answer: ')
        if result == 'n':
            checklen = True
        elif len(result) == len(memo):
            checklen = True
    checknum = False
    if result == 'n':
        checknum = True
    while checknum == False:
        plot = []
        c = 0
        for i in range(len(memo)):
            if int(result[i]) == int(memo[i]):
                plot.append(1)
            else:
                plot.append(0)
                c += 1
        checknum = True
    clearscreen()
    try:
        print(memo)
        print(np.array(list(result)))
        print(np.array(plot))
        print(f'Miss: {c}')
    except:
        clearscreen()
        print('No answer!')


def main():
    print(f'WELCOME TO MEMORY TRAINER VERSION {ver}')
    sleep(1)
    again = True
    while again == True:
        clearscreen()
        user = int(input('Choose your stage (0, 1, 2, 3, 4, 5): '))
        compare(user*10)
        quest = input('Play again? (y/n): ')
        if quest == 'n':
            clearscreen()
            print('Try harder next time!')
            print(f'Author: {auth}')
            sleep(1)
            clearscreen()
            again = False


main()
