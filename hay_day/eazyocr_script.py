import easyocr
import cv2
import numpy as np

# Initialize EasyOCR reader with English language
reader = easyocr.Reader(['en'])

# Path to the image
image_path = 'hay_day_barn/itsmebarn.png'

# Load the image using OpenCV
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding (more flexible than global thresholding)
thresh_image = cv2.adaptiveThreshold(gray_image, 255, 
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 11, 2)

# Optional: Remove noise using a median filter
thresh_image = cv2.medianBlur(thresh_image, 3)

# Perform OCR on the preprocessed image
result = reader.readtext(thresh_image)

# Initialize an empty list to store numbers
numbers = []

# Extract numbers from OCR results
for item in result:
    text = item[1]  # The text part of the result
    if text.isdigit():  # Ensure the text is a valid number
        numbers.append(int(text))  # Convert it to an integer and add to the list

# Sort numbers in descending order
numbers.sort(reverse=True)

# Print the sorted numbers
print("Numbers in descending order:", numbers)
