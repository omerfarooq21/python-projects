import cv2
image = cv2.imread('py1.png')
B,g,R=cv2.split(image)
cv2.imshow('orignal',image)
cv2.imshow('blue',B)
cv2.imshow('green',g)
cv2.imshow('red',R)
cv2.waitKey(0)
cv2.destroyAllWindows()