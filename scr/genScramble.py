#-*- coding:utf-8 -*-
# code reference from https://github.com/BenGotts/Python-Rubiks-Cube-Scrambler

import random

dir1 = ["U", "D", "L", "R", "F", "B"]
dir2 = ["", "'", "2"]
max_len = 25

def gen_scramble():
    sc1 = [[random.choice(dir1), random.choice(dir2)] for x in range(max_len)]
    sc2 = isValid(sc1)

    return list((str(sc2[x][0])+str(sc2[x][1]) for x in range(len(sc2))))

def isValid(array):
    # Exception catch 1(R -> R or R -> R' or R -> R2 ...)
    for x in range(1, len(array)):
        while array[x][0] == array[x-1][0]:
            array[x][0] = random.choice(dir1)
    # Exception catch 2(R -> L -> R or R -> L -> R2 ...)
    for x in range(2, len(array)):
        while array[x][0] == array[x-2][0] or array[x][0] == array[x-1][0]:
            array[x][0] = random.choice(dir1)
    return array

def _debug():
    test = gen_scramble()
    b = True

    for x in range(1, len(test)):
        if test[x][0] == test[x-1][0]:
            b = False
    for x in range(2, len(test)):
        if test[x][0] == test[x-2][0]:
            b = False
    
    if b:
        print(test)
        print('Test passed.')
    else:
        print('Failed.')