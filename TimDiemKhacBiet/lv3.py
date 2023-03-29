import cv2

# Load the image
img = cv2.imread('1.jpg')

# Define the coordinates of the object to be flipped
x, y, w, h = 100, 100, 200, 200

# Extract the object from the image
obj = img[y:y+h, x:x+w]

# Flip the object horizontally
flipped_obj = cv2.flip(obj, 1)

# Replace the original object with the flipped object in the image
img[y:y+h, x:x+w] = flipped_obj

# Display the modified image
cv2.imshow('Modified Image', img)
cv2.waitKey(0)

# Save the modified image
