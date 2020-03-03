import socket

import json

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Woody_ip = '192.168.1.156'
Woody_rece_port = 9902

Woody = ('192.168.1.156', 9902)
Rin = ("192.168.1.80", 9901)

local = ('127.0.0.1', 9999)

sr.bind(Rin)
 
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def sendto_Woody(data):
    data = json.dumps(data)
    #data.encode()
    ss.sendto(data.encode(), Woody)

def rece_Woody(data):
    data,addr = sr.recvfrom(64000)



if __name__ == '__main__':
	print(get_local_ip())
