import socket

import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Woody = ('192.168.1.156', 9902)
Rin = ("192.168.1.80", 9902)

Server_ip = '192.168.1.83'
Server_video_port_rin = 9901

Server_video_woody = (Server_ip, Server_video_port_rin)

s.bind(Rin)

class Face(object):

    def __init__(self):
        self.ip = get_local_ip()
 
def get_local_ip():
    try:
        s_t = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s_t.connect(('8.8.8.8', 80))
        ip = s_t.getsockname()[0]
    finally:
        s_t.close()

    return ip

def sendto(data):
    data = json.dumps(data)
    #data.encode()
    s.sendto(data.encode(), Woody)

def rece():
    raw_data,addr = s.recvfrom(64000)
    data = json.loads(raw_data.decode())
    return data

def sendto_Server_img(image):
    s.sendto(image, Server_video_woody)

if __name__ == '__main__':
	print(get_local_ip())
