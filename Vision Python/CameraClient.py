import socket
import sys
import cv2
import pickle
import numpy as np
import struct

IP='localhost'
PORT=8012


def receive_video(_strHOST, _iPORT):
    #if len(sys.argv) > 0:
        #HOST = sys.argv[0]
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print('Socket created')

    s.bind((_strHOST,_iPORT))
    print ('Socket bind complete')
    while True:
        data, addr = s.recvfrom(360181)
        cv2.waitKey(1)

        frame = pickle.loads(data)
        decompress = cv2.imdecode(frame, 1)
        decompress = cv2.resize(decompress, (1280,1024), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('frame', decompress)
    s.close()
    #else :
    #    print("Provide host IP")

receive_video(IP, PORT)
cv2.destroyAllWindows()