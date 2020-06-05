import picamera
import picamera.array
from time import sleep
import cv2

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

def main():
    pass


def vision():

    camera = picamera.PiCamera()

    res_w = 320
    res_h = 240

    camera.resolution = (res_w, res_h)
    rawCapture = picamera.array.PiRGBArray(camera)

    face_cascade = cv2.CascadeClassifier('Rin_vision/haarcascade_frontalface_alt.xml')
    rectangleColor = (0,165,255) 

    sleep(0.1)

    global a
    global b

    global flag_s

    n = Rf.Neutual()

    for frame in camera.capture_continuous(rawCapture,format='bgr',use_video_port=True):
        image = frame.array

        cv2.flip(image, -1, image)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        maxArea = 0  
        x = 0  
        y = 0  
        w = 0  
        h = 0

        for (_x,_y,_w,_h) in faces:

            if _w*_h > maxArea:
                x = _x
                y = _y
                w = _w
                h = _h
                maxArea = w*h
        if maxArea > 0:
            cv2.rectangle(image,(x,y),(x+w,y+h),rectangleColor,4)
            a = x+w/2 - res_w/2
            b = y+h/2 - res_h/2

            flag_s = 1
            
            n.move_eye(a, b)

        cv2.imshow('img',image)

        n.print_face()
          
        rawCapture.truncate(0)
        if cv2.waitKey(20) & 0xFF == ord('q'):
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



if __name__ == "__main__":

    thre_v = threading.Thread(target = vision)
    thre_m = threading.Thread(target = motion)
    thre_ns = threading.Thread(target = network_s)
    thre_nr = threading.Thread(target = network_r)

    thre_v.start()
    thre_m.start()
    thre_ns.start()
    thre_nr.start()
