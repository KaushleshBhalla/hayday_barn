import cv2 as cv

img = cv.imread('hay_day_barn/itsmebarn.png') 

#cv.imshow('itsmebarn', img)

def rescaleframe(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale )
    dimensions = (width,height) 


    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Test the rescale function
resized_img = rescaleframe(img, scale=0.44)
cv.imshow('Resized Image', resized_img)
cv.waitKey(7000)
