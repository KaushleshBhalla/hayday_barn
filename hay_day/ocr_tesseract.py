import cv2
import pytesseract

# Load the image
img = cv2.imread('hay_day_barn/itsmebarn.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find contours
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# Initialize an empty array
numbers = []

# Iterate through the contours
for c in cnts:
    # Get the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(c)

    # Check if the contour is large enough to be a number
    if w >= 10 and h >= 10:
        # Extract the ROI
        ROI = thresh[y:y+h, x:x+w]

        # Perform OCR on the ROI
        text = pytesseract.image_to_string(ROI, config='--psm 10')

        # Check if the extracted text is a number
        try:
            number = int(text)
            # Append the number to the array
            numbers.append(number)
        except:
            pass

# Print the array of numbers
print(numbers)