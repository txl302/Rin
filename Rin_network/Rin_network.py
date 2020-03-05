import socket

import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Woody = ('192.168.1.156', 9902)
Rin = ("192.168.1.80", 9902)

s.bind(Rin)
 
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

if __name__ == '__main__':
	print(get_local_ip())
