import socket
import sys
import cv2
import pickle
import numpy as np
import struct

HOST='localhost'
PORT=8012

def WaitAndReceiveVideoStream(_strHOST, _iPORT):
    u"""
    Funkcja odbierająca stream z kamery klienta.

    """
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print('Socket created')

    s.bind((_strHOST,_iPORT))
    print ('Socket bind complete')



    data = ""
    #payload_size = struct.calcsize("L")

    i = 0
    while True:
        data, addr = s.recvfrom(512)
        frame=pickle.loads(data)
        i = i + 1
        #frame = numpy.fromstring(data, dtype=numpy.uint8)
        #frame = numpy.reshape(frame, (240,320,3))
        #if 3 == i :
        #    cv2.SaveImage("C:\\image.",frame)
        cv2.imshow('frame',frame)
        cv2.waitKey(4) #Important delay - for test try 2 or 4 value.
        if cv2.waitKey( 1 ) & 0xFF == ord( 'q' ):
            break
    s.close( )

WaitAndReceiveVideoStream(HOST, PORT)