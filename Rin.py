import picamera
import picamera.array
from time import sleep
import cv2

import numpy as np

from Rin_motion import Rin_motion as Rm
from Rin_network import Rin_network as Rn

from Rin_embedded import Rin_faces as Rf

import time

import threading

import socket

current_pos_1 = 90
current_pos_2 = 90

init_pos = [90, 90]

data = [0, 0]

flag_s = 0
flag_n = 0

a = 0
b = 0

a_n = 0
b_n = 0

class Robot(object):

    def __init__(self, rob_id, rob_ip):
        self.rob_id = rob_id
        self.rob_ip = rob_ip

class Rin(Robot):
    pass



def vision_send():
    camera = picamera.PiCamera()

    res_w = 320
    res_h = 240

    camera.resolution = (res_w, res_h)
    rawCapture = picamera.array.PiRGBArray(camera)

    sleep(0.1)


    for frame in camera.capture_continuous(rawCapture,format='bgr',use_video_port=True):
        image = frame.array

        cv2.flip(image, -1, image)

        result, imgencode = cv2.imencode('.jpg',image)
        data_encode = np.array(imgencode)
        str_encode = data_encode.tostring()
        
        Rn.sendto_Server_img(str_encode)
        
        #cv2.imshow('img',image)
          
        rawCapture.truncate(0)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

def rece_motion():

    n = Rf.Neutral()

    while True:
        print('a')

        command_rin = Rn.rece()

        print('b')

        a = command_rin[0]
        b = command_rin[1]

        n.move_eye(-round(int(a)/12), round(int(b)/8))
        n.print_face()

        time.sleep(0.1)


def server_test():
    print('hello!')
    while True:

        ret, img = cap.read()
     
        cv2.imshow('img',img)

        result, imgencode = cv2.imencode('.jpg',img)
        data_encode = np.array(imgencode)
        str_encode = data_encode.tostring()
        
        Wn.sendto_Server_img(str_encode)
        
        k = cv2.waitKey(50) & 0xff
        if k == 27:
            break

def motion():
    Rm.init()

    current_pos_1 = 90
    current_pos_2 = 90

    global a
    global b

    global flag_s
    global flag_n

    global a_n
    global b_n

    while True:
        #print(flag_s, flag_n, flag_s == 0, flag_n == 1, (flag_s == 0) & (flag_n == 1))

        if(flag_s == 1):
            
            if(a < -30):
                current_pos_1 = current_pos_1 + 4
                Rm.move_to(1, current_pos_1)
            if(a > 30):
                current_pos_1 = current_pos_1 - 4
                Rm.move_to(1, current_pos_1)

            if(b < -30):
                current_pos_2 = current_pos_2 + 4
                Rm.move_to(2, current_pos_2)
            if(b > 30):
                current_pos_2 = current_pos_2 - 4
                Rm.move_to(2, current_pos_2)

            flag_s = 0
            
        if((flag_s == 0) & (flag_n == 1)):

            print('network')

            if(a_n < -30):
                current_pos_1 = current_pos_1 + 4
                Rm.move_to(1, current_pos_1)
            if(a_n > 30):
                current_pos_1 = current_pos_1 - 4
                Rm.move_to(1, current_pos_1)

            if(b_n < -30):
                current_pos_2 = current_pos_2 + 4
                Rm.move_to(2, current_pos_2)
            if(b_n > 30):
                current_pos_2 = current_pos_2 - 4
                Rm.move_to(2, current_pos_2)

            flag_n = 0
            
            
        
        time.sleep(0.02)

def network_r():
    global flag_n

    global a_n
    global b_n

    while True:

        data = Rn.rece()

        flag_n = 1

        a_n = data[0]
        b_n = data[1]

        print(a_n, b_n)

        time.sleep(0.02)

def network_s():
    global flag_n

    global a
    global b
    
    while True:
        while(flag_s == 1):
            data = [a,b]
            Rn.sendto(data)

            time.sleep(0.02)


def test():

    thre_v = threading.Thread(target = vision_send)
    thre_m = threading.Thread(target = rece_motion)

    thre_v.start()
    thre_m.start()


def demo():
    thre_v = threading.Thread(target = vision)
    thre_m = threading.Thread(target = motion)
    thre_ns = threading.Thread(target = network_s)
    thre_nr = threading.Thread(target = network_r)

    thre_v.start()
    thre_m.start()
    thre_ns.start()
    thre_nr.start()





if __name__ == "__main__":
    test()
    #vision_send()

