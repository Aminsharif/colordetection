import cv2

from util import get_limits

cap =cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame', frame)

    lower_limit, upper_limit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        quit

cap.release()


