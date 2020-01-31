import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

woody = ("192.168.1.87", 9901)

sr.bind(woody)
 
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def sendto_woody(data):
    ss.sendto(data, woody)

def rece_woody(data):
    data,addr = sr.recvfrom(64000)



if __name__ == '__main__':
	print(get_local_ip())
