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

def audio_send():
    pass

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



def test():

    thre_v = threading.Thread(target = vision_send)
    thre_m = threading.Thread(target = rece_motion)

    thre_v.start()
    thre_m.start()



if __name__ == "__main__":
    test()
    #vision_send()

