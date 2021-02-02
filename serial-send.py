# Author: Muhammad Zulfaqar bin Azmi
# Email: mzulfaqar88@gmail.com
#import pdb
import socket
from time import sleep
import pickle

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello world"
def createMessage():
    #data = [i for i in range(5)]
    data = MESSAGE
    return pickle.dumps(data) 

if __name__ == "__main__":
    # pdb.set_trace()
    while True:
        print(f"Sending {pickle.loads(createMessage())} UDP target IP:PORT = {UDP_IP}:{UDP_PORT}")

        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
        sock.sendto(createMessage(),
                    (UDP_IP, UDP_PORT))
        sleep(1)
        #  LocalWords:  UDP createMessage
