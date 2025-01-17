import cv2 as cv

# img = cv.imread('hay_day_barn/IMG_1912.png') 

# cv.imshow('img_1912', img)

# cv.waitKey(0)

capture = cv.VideoCapture(0)
while True:
    isTrue, frame  = capture.read()
    cv.imshow('video', frame)

    key = cv.waitKey(20) & 0xFF
    if key == ord(' ') or key == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
