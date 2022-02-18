import cv2 as cv

# img = cv.imread('C:/Users/sangmin/Desktop/aigo.jpg')

# cv.imshow('aigo', img)

# cv.waitKey(0)

# reading video

capture = cv.VideoCapture('D:/유투브영상다운/j.fla/fiestar.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.realese()
cv.waitKey(0)