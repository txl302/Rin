import os
import sys
import time
import random
from collections import namedtuple

SHOW = '\033[32m#'
EMPTY = ' '


class Face(object):

    def __init__(self):
        self.height = 30
        self.width = 80
        self.eye_height = 12
        self.eye_width = 18
        self.eye_off = [0, 0]
        self.rows = []
        for _ in range(self.height):
            self.rows.append([SHOW] * self.width)

class Neutral(Face):

    def print_face(self):
        self.rows = []
        for i in range(self.height):
            if ((i+1)<=(self.height/2-self.eye_height/2+self.eye_off[1]) or (i+1)>(self.height/2 + self.eye_height/2+self.eye_off[1])):
                self.rows.append([EMPTY] * self.width)
            else:
                self.rows.append([EMPTY]*round(self.width/4-self.eye_width/2+self.eye_off[0]) + [SHOW]*self.eye_width + [EMPTY]*round(self.width/2-self.eye_width) + [SHOW]*self.eye_width + [EMPTY]*round(self.width/4-self.eye_width/2-self.eye_off[0]))
        
        clear = '\x1b[{}A\x1b[{}D'.format(self.height,self.width) 
        print(clear)
        print(self)
        time.sleep(.1)
    
    def normal(self):
        self.eye_height = 12
        self.eye_width = 18
        self.eye_off = [0, 0]
        self.print_face()

    def close(self):
        self.eye_height = 2
        self.eye_width = 20
        self.print_face()

    def move_eye(self, x, y):
        self.eye_off[0] = x
        self.eye_off[1] = y
        self.print_face()

    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output     


class Happy(Face):

    def print_face(self):
        self.rows = []
        for i in range(self.height):
            if ((i+1)<=(self.height/2-self.eye_height/2+self.eye_off[1]) or (i+1)>(self.height/2 + self.eye_height/2+self.eye_off[1])):
                self.rows.append([EMPTY] * self.width)
            else:
                side = round(self.width/4-self.eye_width/2+0.6*(self.width/self.height)*(i-self.height/2+self.eye_height/2))
                self.rows.append([EMPTY]*side + [SHOW]*2 + [EMPTY]*(self.width-side*2-4) + [SHOW]*2 + [EMPTY]*side)
        
        clear = '\x1b[{}A\x1b[{}D'.format(self.height,self.width) 
        print(clear)
        print(self)
        time.sleep(.1)
    
    def normal(self):
        self.eye_height = 12
        self.eye_width = 18
        self.eye_off = [0, 0]
        self.print_face()

    def move_eye(self, x, y):
        self.eye_off[0] = x
        self.eye_off[1] = y
        self.print_face()

    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output  

class Angry(Face):

    def print_face(self):
        self.rows = []
        for i in range(self.height):
            if ((i+1)<=(self.height/2-self.eye_height/2+self.eye_off[1]) or (i+1)>(self.height/2 + self.eye_height/2+self.eye_off[1])):
                self.rows.append([EMPTY] * self.width)
            else:
                
                #print(round(self.width/self.height)*(i-self.height/2+self.eye_height/2))
                side = round(self.width/4-self.eye_width/2+0.6*(self.width/self.height)*(i-self.height/2+self.eye_height/2))
                self.rows.append([EMPTY]*side + [SHOW]*2 + [EMPTY]*(self.width-side*2-4) + [SHOW]*2 + [EMPTY]*side)
                
        clear = '\x1b[{}A\x1b[{}D'.format(self.height,self.width) 
        print(clear)
        print(self)
        time.sleep(.1)
    
    def normal(self):
        self.eye_height = 12
        self.eye_width = 18
        self.eye_off = [0, 0]
        self.print_face()

    def move_eye(self, x, y):
        self.eye_off[0] = x
        self.eye_off[1] = y
        self.print_face()

    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output  


class Sad(Face):

    def print_face(self):
        self.rows = []
        for i in range(self.height):
            if ((i+1)<=(self.height/2-self.eye_height/2+self.eye_off[1]) or (i+1)>(self.height/2 + self.eye_height/2+self.eye_off[1])):
                self.rows.append([EMPTY] * self.width)
            else:
                
                #print(round(self.width/self.height)*(i-self.height/2+self.eye_height/2))
                side = round(self.width/2) - round(self.width/4-self.eye_width/2+0.6*(self.width/self.height)*(i-self.height/2+self.eye_height/2))
                #print(side)
                self.rows.append([EMPTY]*side + [SHOW]*2 + [EMPTY]*(self.width-side*2-4) + [SHOW]*2 + [EMPTY]*side)
        
        clear = '\x1b[{}A\x1b[{}D'.format(self.height,self.width) 
        print(clear)
        print(self)
        time.sleep(.1)
    
    def normal(self):
        self.eye_height = 12
        self.eye_width = 18
        self.eye_off = [0, 0]
        self.print_face()

    def move_eye(self, x, y):
        self.eye_off[0] = x
        self.eye_off[1] = y
        self.print_face()

    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output  


class Happy(Face):

    def print_face(self):
        self.rows = []
        for i in range(self.height):
            if ((i+1)<=(self.height/2-self.eye_height/2+self.eye_off[1]) or (i+1)>(self.height/2 + self.eye_height/2+self.eye_off[1])):
                self.rows.append([EMPTY] * self.width)
            else:
                side = round(self.width/4 - (self.eye_width/2)*(i-(self.height-self.eye_height)/2)*(self.width-self.eye_width)/2/self.eye_height)
                inner = round((self.eye_width/2)*(i-(self.height-self.eye_height)/2)*(self.width-self.eye_width)/2/self.eye_height)
                print(side, inner)
                self.rows.append([EMPTY]*side + [SHOW]*2 + [EMPTY]*inner + [SHOW])
        
        clear = '\x1b[{}A\x1b[{}D'.format(self.height,self.width) 
        #print(clear)
        #print(self)
        time.sleep(.1)
    
    def normal(self):
        self.eye_height = 12
        self.eye_width = 18
        self.eye_off = [0, 0]
        self.print_face()

    def move_eye(self, x, y):
        self.eye_off[0] = x
        self.eye_off[1] = y
        self.print_face()

    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output 


def neutral_test():
    os.system('clear')
    n = Neutral()
    while True:
        n.close()
        n.normal()
        n.close()
        n.normal()
        time.sleep(2)
        n.move_eye(-2, -2)
        time.sleep(2)
        n.move_eye(2, -2)
        time.sleep(2)
        n.normal()
        time.sleep(2)

def angry_test():
    os.system('clear')
    a = Angry()
    while True:
        a.normal()
        time.sleep(2)
        a.move_eye(-2, -2)
        time.sleep(2)
        a.move_eye(2, -2)
        time.sleep(2)
        a.normal()
        time.sleep(2)

def sad_test():
    os.system('clear')
    s = Sad()
    while True:
        s.normal()
        time.sleep(2)
        s.move_eye(-2, -2)
        time.sleep(2)
        s.move_eye(2, -2)
        time.sleep(2)
        s.normal()
        time.sleep(2)

def happy_test():
    os.system('clear')
    h = Happy()
    while True:
        h.normal()
        time.sleep(2)
        h.move_eye(-2, -2)
        time.sleep(2)
        h.move_eye(2, -2)
        time.sleep(2)
        h.normal()
        time.sleep(2)

def demo():
    os.system('clear')
    n = Neutral()
    a = Angry()
    s = Sad()
    while True:
        n.close()
        n.normal()
        n.close()
        n.normal()
        time.sleep(2)
        n.move_eye(-2, -2)
        time.sleep(2)
        n.move_eye(2, -2)
        time.sleep(2)
        n.normal()
        time.sleep(2)

        n.close()
        n.normal()
        n.close()
        n.normal()
        time.sleep(2)

        a.normal()
        time.sleep(2)

        n.close()
        n.normal()
        n.close()
        n.normal()
        time.sleep(2)

        s.normal()
        time.sleep(2)






if __name__ == '__main__':
    #demo()

    happy_test()