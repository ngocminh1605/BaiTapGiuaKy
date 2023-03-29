import cv2
import random

img = cv2.imread('1.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(img_gray, 150, 200)
# Find contours
contours, _ = cv2.findContours(img_canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area = cv2.contourArea(random.choice(contours))
x, y, w, h = cv2.boundingRect(random.choice(contours))
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
b,g,r = img[x,y]
img[y:y+h, x:x+w] = (b,g,r) 
cv2.imshow('Detected Contours', img)
cv2.imwrite('lv3.jpg',img)
cv2.waitKey(0)
