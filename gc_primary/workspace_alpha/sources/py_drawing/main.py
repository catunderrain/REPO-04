
from time import sleep
import os
sq = {}
sq[0] = ['oooooooooooooooooooo',
         'o                  o',
         'o     xx    xx     o',
         'o   x    xx    x   o',
         'o   x          x   o',
         'o     x       x    o',
         'o       x   x      o',
         'o        xx        o',
         'oooooooooooooooooooo']
sq[1] = ['  oooooooooooooooo  ',
         '  o              o  ',
         '  o              o  ',
         '  o              o  ',
         '  o              o  ',
         '  o              o  ',
         '  o              o  ',
         '  o              o  ',
         '  oooooooooooooooo  ']
sq[2] = ['    oooooooooooo    ',
         '    o          o    ',
         '    o          o    ',
         '    o          o    ',
         '    o          o    ',
         '    o          o    ',
         '    o          o    ',
         '    o          o    ',
         '    oooooooooooo    ']
sq[3] = ['      oooooooo      ',
         '      o      o      ',
         '      o      o      ',
         '      o      o      ',
         '      o      o      ',
         '      o      o      ',
         '      o      o      ',
         '      o      o      ',
         '      oooooooo      ']
sq[4] = ['        oooo        ',
         '        o  o        ',
         '        o  o        ',
         '        o  o        ',
         '        o  o        ',
         '        o  o        ',
         '        o  o        ',
         '        o  o        ',
         '        oooo        ', ]
sq[5] = ['         oo         ',
         '         oo         ',
         '         oo         ',
         '         oo         ',
         '         oo         ',
         '         oo         ',
         '         oo         ',
         '         oo         ',
         '         oo         ']


def pr(x):
    for i in range(len(x)):
        print(x[i])


while True:
    num = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
    for i in num:
        print('Your computer is hacked!')
        pr(sq[i])
        sleep(0.05)
        os.system('cls')
