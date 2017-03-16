import cv2
import numpy as np
import socket
import pickle
import sys

IP = ""
PORT = 8012

cap=cv2.VideoCapture(0)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
if(len(sys.argv) > 1):
    IP = sys.argv[1]

    while (True):
        ret, frame = cap.read()

        if cap.isOpened():
            frame = cv2.resize(frame, (400,300), interpolation=cv2.INTER_CUBIC)

            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            result, compress = cv2.imencode('.jpg', frame, encode_param)

            data = np.array(compress)
            dataToSend = pickle.dumps(data)

            sock.sendto(dataToSend, (IP, PORT))
        else:
            print("No camera found")
            break
else :
    print("Give IP")

cap.release()

