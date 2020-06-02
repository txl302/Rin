import os
import sys
import time
import random
from collections import namedtuple


SHOW = '\033[36m#'
EMPTY = ' '



class Face(object):

    def __init__(self):
        self.height = 32
        self.width = 80
        self.rows = []
        for _ in range(self.height):
            self.rows.append([SHOW] * self.width)

    def neutral(self):
        self.rows = []
        for i in range(self.height):
            if (i<6 or i>25):
                self.rows.append([EMPTY] * self.width)
            else:
                self.rows.append([EMPTY]*12 + [SHOW]*16 + [EMPTY]*24 + [SHOW]*16 + [EMPTY]*12)

    def close(self):
        self.rows = []
        for i in range(self.height):
            if (i<15 or i>16):
                self.rows.append([EMPTY] * self.width)
            else:
                self.rows.append([EMPTY]*10 + [SHOW]*20 + [EMPTY]*20 + [SHOW]*20 + [EMPTY]*10)

    def twinkle(self):

        clear = '\x1b[{}A\x1b[{}D'.format(80,32)
        self.close()

        print(clear)
        print(self)
        time.sleep(.1)

        self.neutral()

        print(clear)
        print(self)
        time.sleep(.1)

        self.close()

        print(clear)
        print(self)
        time.sleep(.1)

        self.neutral()

        print(clear)
        print(self)
        time.sleep(2)

    def look_left(self):
        self.rows = []
        for i in range(self.height):
            if (i<3 or i>22):
                self.rows.append([EMPTY] * self.width)
            else:
                self.rows.append([EMPTY]*6 + [SHOW]*16 + [EMPTY]*24 + [SHOW]*16 + [EMPTY]*18)

    def look_right(self):
        self.rows = []
        for i in range(self.height):
            if (i<3 or i>22):
                self.rows.append([EMPTY] * self.width)
            else:
                self.rows.append([EMPTY]*18 + [SHOW]*16 + [EMPTY]*24 + [SHOW]*16 + [EMPTY]*6)

    def look_around(self):
        clear = '\x1b[{}A\x1b[{}D'.format(80,32)
        self.look_left()

        print(clear)
        print(self)
        time.sleep(1)

        self.look_right()

        print(clear)
        print(self)
        time.sleep(1)

        self.neutral()

        print(clear)
        print(self)
        time.sleep(1)

    def normal(self):
        clear = '\x1b[{}A\x1b[{}D'.format(80,32)

        self.neutral()

        print(clear)
        print(self)
        time.sleep(1)







    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output     



def test():
    os.system('clear')
    g = Face()
    clear = '\x1b[{}A\x1b[{}D'.format(80,32)
    while True:
        g.normal()
        g.look_around()
        g.twinkle()
        g.twinkle()



        


    


if __name__ == '__main__':
    test()