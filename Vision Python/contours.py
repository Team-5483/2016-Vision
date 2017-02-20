import cv2
import numpy as np
import socket
import struct
cap = cv2.VideoCapture(0)

HOST = "127.0.0.1"
PORT = 7070

sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

sock.connect((HOST, PORT))

while(1):
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower = np.array([80, 60, 120])
    #upper = np.array([90, 200, 200])
    lower = np.array([60, 100, 100])
    upper = np.array([90, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    ret, thresh = cv2.threshold(mask, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)



    if not len(contours) == 0:
        cnt = contours[0]
        #rect = cv2.minAreaRect( cnt )
        #box = cv2.boxPoints( rect )
        #box = np.int0( box )
        #cv2.drawContours( frame, [box], 0, (0, 0, 255), 2 )
        largest = 0
        secondLargest = 0
        for i in range(len(contours)):
            if cv2.contourArea(contours[i]) > cv2.contourArea(contours[largest]):
                largest = i
            elif cv2.contourArea(contours[i]) > cv2.contourArea(contours[secondLargest]):
                secondLargest = i

        x, y, w, h = cv2.boundingRect(contours[largest])
        cv2.rectangle( frame, (x, y), (x + w, y + h), (0, 0, 255), 2 )

        x2, y2, w2, h2 = cv2.boundingRect(contours[secondLargest])
        cv2.rectangle( frame, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2 )

        print(x)

        #detect peg

        #Are sizes similar?
        if h-100<h2<h+100 and w-100<w2<w+100 and w > 10 and h > 10 and w2 > 10 and h2 > 10:
            xpos = int(abs(x+w+x2)/2)
            ypos = int(y)
            cv2.circle(frame, (xpos,ypos), 20, (255,0,255),-1)
            #P for peg
            sock.send(b"P:" + str(xpos).encode() + b" " + str(ypos).encode())

    cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
