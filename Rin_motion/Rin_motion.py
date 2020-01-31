from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)

def move_to(num, pos):
    kit.servo[num].angle = pos

def init():
    move_to(1, 90)
    move_to(2, 90)
