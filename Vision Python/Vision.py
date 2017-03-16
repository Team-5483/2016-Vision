import cv2
import numpy as np
import socket
import sys
import pickle
cap = cv2.VideoCapture(0)

RioIP = ""
RioPORT = 7070

RioSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

LaptopIP = ""
LaptopPORT = 6969

LaptopSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if len(sys.argv) > 2:
    LaptopIP = sys.argv[1]
    RioIP = sys.argv[2]
    RioSock.connect((RioIP, RioPORT))
    LaptopSock.connect((LaptopIP,LaptopPORT))
    #lower = np.array([80, 60, 120])
    #upper = np.array([90, 200, 200])
    lower = np.array([60, 100, 100])
    upper = np.array([90, 255, 255])

    if len(sys.argv) == 8:
        slower = sys.argv[2:5]
        supper = sys.argv[5:8]

        lower = np.array(list(map(int, slower)))
        upper = np.array(list(map(int, supper)))

    else:
        print("No colours provided, going to default")

    while True:
        _, frame = cap.read()
        if cap.isOpened():

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(hsv, lower, upper)

            ret, thresh = cv2.threshold(mask, 127, 255, 0)
            im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

            if not len(contours) == 0:
                cnt = contours[0]

                largest = 0
                secondLargest = 0
                for i in range(len(contours)):
                    if cv2.contourArea(contours[i]) > cv2.contourArea(contours[largest]):
                        largest = i
                    elif cv2.contourArea(contours[i]) > cv2.contourArea(contours[secondLargest]):
                        secondLargest = i

                x, y, w, h = cv2.boundingRect(contours[largest])
                #cv2.rectangle( frame, (x, y), (x + w, y + h), (0, 0, 255), 2 )

                x2, y2, w2, h2 = cv2.boundingRect(contours[secondLargest])
                #cv2.rectangle( frame, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2 )


                #Are sizes similar?
                if h-100<h2<h+100 and w-100<w2<w+100 and w > 10 and h > 10 and w2 > 10 and h2 > 10:
                    xpos = int(abs(x+w+x2)/2)
                    ypos = int(y)
                    #cv2.circle(frame, (xpos,ypos), 20, (255,0,255),-1)

                    if(x < x2):
                        wright = w
                        wleft = w2
                    else:
                        wright = w2
                        wleft = w

                    #P for peg
                    RioSock.send(b"P:" + str(xpos).encode() + b" " + str(ypos).encode() + b" " + str(wleft).encode() + b" "
                              + str(wright).encode())

            #compress frame and send to laptop
            frame = cv2.resize(frame, (400, 300), interpolation=cv2.INTER_CUBIC)

            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            result, compress = cv2.imencode('.jpg', frame, encode_param)

            data = np.array(compress)
            dataToSend = pickle.dumps(data)

            LaptopSock.send(dataToSend)

        else:
            print("No camera found")
            break
else:
    print("Give laptop and rio IP")
cv2.destroyAllWindows()
