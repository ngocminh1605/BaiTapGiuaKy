import cv2

# Load the image
img = cv2.imread('1.jpg')

# Define the center and radius of the circle
center = (50, 50)
radius = 50

# Draw the circle on the image
cv2.circle(img, center, radius, (0, 0, 255), 2)

# Display the image
cv2.imshow('image1', img)
# cv2.imwrite('output_image.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

