# Author: Muhammad Zulfaqar bin Azmi
# Email: mzulfaqar88@gmail.com
import socket
import pickle
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.settimeout(1.5)
sock.bind((UDP_IP,
           UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024)
    print(f"Receiving message: {pickle.loads(data)}, with type {type(pickle.loads(data))}")
