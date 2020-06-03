import os
import sys
import time
import random
from collections import namedtuple


SHOW = '\033[32m#'
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
            if (i<8 or i>25):
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

    def sad(self):
        self.rows = []
        for i in range(self.height):
            if (i<8 or i>25):
                self.rows.append([EMPTY] * self.width)
            else:
                for j in range(self.width):
                    self.rows.append()

    def Tingbaobao(self):
        self.rows = []

        for i in range(self.height):
            if (i<7 or i>19):
                self.rows.append([EMPTY] * self.width)
            if (i==7):
                self.rows.append([EMPTY]*4 + ([EMPTY]*24)+([EMPTY]*10+[SHOW]*1+[EMPTY]*13) + ([EMPTY]*10+[SHOW]*1+[EMPTY]*13))
            if (i==8):
                self.rows.append([EMPTY]*4 + ([EMPTY]*24)+([EMPTY]*11+[SHOW]*1+[EMPTY]*12) + ([EMPTY]*11+[SHOW]*1+[EMPTY]*12))
            if (i==9):
                self.rows.append([EMPTY]*4 + ([EMPTY]+[SHOW]*5+[EMPTY]+[SHOW]*3+[EMPTY]+[SHOW]*2+[EMPTY]*3+[SHOW]+[EMPTY]+[SHOW]*4+[EMPTY]*2)+([EMPTY]*2+[SHOW]*18+[EMPTY]*4) + ([EMPTY]*2+[SHOW]*18+[EMPTY]*4))
            if (i==10):
                self.rows.append([EMPTY]*4 + ([EMPTY]*3+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*2+[SHOW]*2+[EMPTY]*3+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]*2)+([EMPTY]*2+[SHOW]*1+[EMPTY]*16+[SHOW]*1+[EMPTY]*4) + ([EMPTY]*2+[SHOW]*1+[EMPTY]*16+[SHOW]*1+[EMPTY]*4))
            if (i==11):
                self.rows.append([EMPTY]*4 + ([EMPTY]*3+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*5)+([EMPTY]*6+[SHOW]*10+[EMPTY]*8) + ([EMPTY]*6+[SHOW]*10+[EMPTY]*8))
            if (i==12):
                self.rows.append([EMPTY]*4 + ([EMPTY]*3+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*5)+([EMPTY]*10+[SHOW]*2+[EMPTY]*12) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*12))
            if (i==13):
                self.rows.append([EMPTY]*4 + ([EMPTY]*3+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*5)+([EMPTY]*10+[SHOW]*2+[EMPTY]*12) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*12))
            if (i==14):
                self.rows.append([EMPTY]*4 + ([EMPTY]*3+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]+[SHOW]*3+[EMPTY])+([EMPTY]*6+[SHOW]*10+[EMPTY]*8) + ([EMPTY]*6+[SHOW]*10+[EMPTY]*8))
            if (i==15):
                self.rows.append([EMPTY]*4 + ([EMPTY]*3+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]*2)+([EMPTY]*10+[SHOW]*2+[EMPTY]*12) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*12))
            if (i==16):
                self.rows.append([EMPTY]*4 + ([EMPTY]*3+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]*3+[SHOW]*2+[EMPTY]+[SHOW]+[EMPTY]*2+[SHOW]+[EMPTY]*2)+([EMPTY]*10+[SHOW]*2+[EMPTY]*2+[SHOW]*1+[EMPTY]*9) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*2+[SHOW]*1+[EMPTY]*9))
            if (i==17):
                self.rows.append([EMPTY]*4 + ([EMPTY]*3+[SHOW]+[EMPTY]*3+[SHOW]*3+[EMPTY]+[SHOW]+[EMPTY]*3+[SHOW]*2+[EMPTY]+[SHOW]*4+[EMPTY]*2)+([EMPTY]*10+[SHOW]*2+[EMPTY]*3+[SHOW]*1+[EMPTY]*8) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*3+[SHOW]*1+[EMPTY]*8))
            if (i==18):
                self.rows.append([EMPTY]*4 + ([EMPTY]*24)+([EMPTY]*10+[SHOW]*2+[EMPTY]*12) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*12))
            if (i==19):
                self.rows.append([EMPTY]*4 + ([EMPTY]*24)+([EMPTY]*2+[SHOW]*18+[EMPTY]*4) + ([EMPTY]*2+[SHOW]*18+[EMPTY]*4))

    def Taobaobao(self):
        self.rows = []

        for i in range(self.height):
            if (i<7 or i>19):
                self.rows.append([EMPTY] * self.width)
            if (i==7):
                self.rows.append([EMPTY]*4 + ([EMPTY]*24)+([EMPTY]*10+[SHOW]*1+[EMPTY]*13) + ([EMPTY]*10+[SHOW]*1+[EMPTY]*13))
            if (i==8):
                self.rows.append([EMPTY]*4 + ([EMPTY]*24)+([EMPTY]*11+[SHOW]*1+[EMPTY]*12) + ([EMPTY]*11+[SHOW]*1+[EMPTY]*12))
            if (i==9):
                self.rows.append([EMPTY]*4 + ([EMPTY]+[SHOW]*7+[EMPTY]+[SHOW]*6+[EMPTY]+[SHOW]*7+[EMPTY]) + ([EMPTY]*2+[SHOW]*18+[EMPTY]*4) + ([EMPTY]*2+[SHOW]*18+[EMPTY]*4))
            if (i==10):
                self.rows.append([EMPTY]*4 + ([EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*5+[SHOW]+[EMPTY]) + ([EMPTY]*2+[SHOW]*1+[EMPTY]*16+[SHOW]*1+[EMPTY]*4) + ([EMPTY]*2+[SHOW]*1+[EMPTY]*16+[SHOW]*1+[EMPTY]*4))
            if (i==11):
                self.rows.append([EMPTY]*4 + ([EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*5+[SHOW]+[EMPTY]) + ([EMPTY]*6+[SHOW]*10+[EMPTY]*8) + ([EMPTY]*6+[SHOW]*10+[EMPTY]*8))
            if (i==12):
                self.rows.append([EMPTY]*4 + ([EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*5+[SHOW]+[EMPTY]) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*12) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*12))
            if (i==13):
                self.rows.append([EMPTY]*4 + ([EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]*6+[EMPTY]+[SHOW]+[EMPTY]*5+[SHOW]+[EMPTY]) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*12) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*12))
            if (i==14):
                self.rows.append([EMPTY]*4 + ([EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*5+[SHOW]+[EMPTY]) + ([EMPTY]*6+[SHOW]*10+[EMPTY]*8) + ([EMPTY]*6+[SHOW]*10+[EMPTY]*8))
            if (i==15):
                self.rows.append([EMPTY]*4 + ([EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*5+[SHOW]+[EMPTY]) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*12) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*12))
            if (i==16):
                self.rows.append([EMPTY]*4 + ([EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]+[SHOW]+[EMPTY]*5+[SHOW]+[EMPTY]) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*2+[SHOW]*1+[EMPTY]*9) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*2+[SHOW]*1+[EMPTY]*9))
            if (i==17):
                self.rows.append([EMPTY]*4 + ([EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]*4+[SHOW]+[EMPTY]+[SHOW]*7+[EMPTY]) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*3+[SHOW]*1+[EMPTY]*8) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*3+[SHOW]*1+[EMPTY]*8))
            if (i==18):
                self.rows.append([EMPTY]*4 + ([EMPTY]*24)+([EMPTY]*10+[SHOW]*2+[EMPTY]*12) + ([EMPTY]*10+[SHOW]*2+[EMPTY]*12))
            if (i==19):
                self.rows.append([EMPTY]*4 + ([EMPTY]*24)+([EMPTY]*2+[SHOW]*18+[EMPTY]*4) + ([EMPTY]*2+[SHOW]*18+[EMPTY]*4))

    def xiao_xin(self):
        self.rows = []

        for i in range(self.height):
            if (i<7 or i>23):
                self.rows.append([EMPTY] * self.width)
            elif (i>=7 and i<=10):
                if (i==7):
                   self.rows.append([EMPTY]*30 + [SHOW]*2 + [EMPTY]*16 + [SHOW]*2 + [EMPTY]*30)
                if (i==8):
                    self.rows.append([EMPTY]*27 + [SHOW]*8 + [EMPTY]*10 + [SHOW]*8 + [EMPTY]*27)
                if (i==9):
                    self.rows.append([EMPTY]*25 + [SHOW]*12 + [EMPTY]*6 + [SHOW]*12 + [EMPTY]*25)
                if (i==10):
                    self.rows.append([EMPTY]*23 + [SHOW]*16 + [EMPTY]*2 + [SHOW]*16 + [EMPTY]*23)
            else:
                self.rows.append([EMPTY]*(2*i) + [SHOW]*(self.width-4*i) + [EMPTY]*(2*i))

    def da_xin(self):
        self.rows = []

        for i in range(self.height):
            if (i<5 or i>28):
                self.rows.append([EMPTY] * self.width)
            elif (i>=5 and i<=8):
                if (i==5):
                   self.rows.append([EMPTY]*28 + [SHOW]*2 + [EMPTY]*20 + [SHOW]*2 + [EMPTY]*28)
                if (i==6):
                    self.rows.append([EMPTY]*25 + [SHOW]*8 + [EMPTY]*14 + [SHOW]*8 + [EMPTY]*25)
                if (i==7):
                    self.rows.append([EMPTY]*22 + [SHOW]*14 + [EMPTY]*8 + [SHOW]*14 + [EMPTY]*22)
                if (i==8):
                    self.rows.append([EMPTY]*19 + [SHOW]*20 + [EMPTY]*2 + [SHOW]*20 + [EMPTY]*19)
            else:
                self.rows.append([EMPTY]*(2*i) + [SHOW]*(self.width-4*i) + [EMPTY]*(2*i))


    def kaixin(self):
        clear = '\x1b[{}A\x1b[{}D'.format(80,32)

        self.Taobaobao()

        print(clear)
        print(self)
        time.sleep(1)

        self.xiao_xin()

        print(clear)
        print(self)
        time.sleep(1)

        self.Tingbaobao()

        print(clear)
        print(self)
        time.sleep(1)

        self.xiao_xin()

        print(clear)
        print(self)
        time.sleep(0.1)

        self.da_xin()

        print(clear)
        print(self)
        time.sleep(0.1)

        self.xiao_xin()

        print(clear)
        print(self)
        time.sleep(0.1)

        self.da_xin()

        print(clear)
        print(self)
        time.sleep(1)





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
        g.kaixin()

def test2():
    os.system('clear')
    g = Face()
    while True:
        g.kaixin()


        


    


if __name__ == '__main__':
    test()