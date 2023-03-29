import cv2
import random

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
img_canny = cv2.Canny(gray, 150, 200)
# Find contours
contours, _ = cv2.findContours(img_canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE,offset=(0,0))

x, y, w, h = cv2.boundingRect(random.choice(contours))
obj = img[y:y+h, x:x+w]
flipped_obj = cv2.flip(obj, 1)
img[y:y+h, x:x+w] = flipped_obj
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Detected Contours', img)
cv2.imwrite('lv2.jpg',img)
cv2.waitKey(0)
