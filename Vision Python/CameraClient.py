import cv2
import numpy as np
import socket
import sys
import pickle
import struct



UDP_IP = "localhost"
UDP_PORT = 8012
cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    ret,frame=cap.read()
    frame = cv2.resize( frame, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_CUBIC )
    #result, img_str = cv2.imencode('.jpeg', frame)
    #img_str2 = np.array(img_str)

    #pik = pickle.Pickler()
    #frame = np.reshape(frame, (240,320,3))
    data = np.array(frame)
    dataToSend = pickle.dumps(data)
    size = sys.getsizeof(dataToSend)
    #print(size)
    #print(type(dataToSend));

    clientsocket.sendto(dataToSend, (UDP_IP, UDP_PORT))

