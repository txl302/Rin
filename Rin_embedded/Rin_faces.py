import os
import sys
import time
import random
from collections import namedtuple


SHOW = '*'
EMPTY = ' '



class Face(object):
    def __init__(self):
        self.height = 32
        self.width = 40
        self.rows = []
        for _ in range(self.height):
            self.rows.append([SHOW] * self.width)

    def neutral(self):
        self.rows = []
        for i in range(self.height):
            if (i<6 or i>25):
                self.rows.append([EMPTY] * self.width)
            else:
                self.rows.append([EMPTY]*6 + [SHOW]*8 + [EMPTY]*12 + [SHOW]*8 + [EMPTY]*6)



    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output     





def test():
    g = Face()
    g.neutral()
    clear = '\x1b[{}A\x1b[{}D'.format(40,32)
    while True:
        print(clear)
        print(g)
        time.sleep(.1)
    


if __name__ == '__main__':
    test()