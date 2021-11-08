import cv2

img = cv2.imread('D:\MaDoc\car.png', 1)
img = img[200:, :]
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.GaussianBlur(img, (5, 5), 0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
canny = cv2.Canny(hsv, 200, 255)

cv2.imshow('Car', img)
cv2.imshow('Gray', gray)
cv2.imshow('Hsv', hsv)
cv2.imshow('Canny', canny)
cv2.waitKey()
cv2.destroyAllWindows()
