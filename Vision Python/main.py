import cv2
import numpy as np
import socket

cap = cv2.VideoCapture(0)

HOST = "127.0.0.1"
PORT = 6969

message = "Coordinates : "

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.connect((HOST, PORT))

#vision
while(1):
    # Take each frame
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.CV_8UC1)

    #lower_green = np.array([80, 60, 120])
    #upper_green = np.array([90, 200, 200])
    lower_green = np.array([0,0,0])
    upper_green = np.array([255,255,255])


    #mask = cv2.inRange(hsv, lower_green, upper_green)
    #sobel = cv2.Sobel(mask, cv2.CV_8UC1, 1, 1, ksize=5)

    ret, thresh = cv2.threshold(hsv, 127, 255, 0)

    im2, contours, hierarchy = cv2.findContours(thresh,  cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    sobel = cv2.drawContours(cap.read, contours, 0, (255, 0, 0), 3)

    dst = cv2.cornerHarris(sobel, 2, 3, 0.04)


    cv2.imshow('frame', frame)
    cv2.imshow('corner', sobel)
    #   res = cv2.bitwise_and(frame, frame, mask= mask)

    #for i in range(len(contours)):
        #message += contours[i]
        #message += " "
    #sock.send(message)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
