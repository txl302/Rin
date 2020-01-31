import picamera
import picamera.array
from time import sleep
import cv2

from Rin_motion import Rin_motion as Rm
from Rin_network import Rin_network as Rn

import time

current_pos_1 = 90
current_pos_2 = 90

init_pos = [90, 90]


def main():

    Rm.init()

    current_pos_1 = 90
    current_pos_2 = 90


    camera = picamera.PiCamera()

    res_w = 320
    res_h = 240

    camera.resolution = (res_w, res_h)
    rawCapture = picamera.array.PiRGBArray(camera)

    face_cascade = cv2.CascadeClassifier('Rin_vision/haarcascade_frontalface_alt.xml')
    rectangleColor = (0,165,255) 

    sleep(0.1)

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

            Rn.sendto_woody([a ,b])
                
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
        else:
            Rn.rece_woody(data)
            a = data[0]
            b = data[1]

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
            
     
        image = cv2.resize(image, (640,480))
        cv2.imshow('img',image)
          
        rawCapture.truncate(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()

