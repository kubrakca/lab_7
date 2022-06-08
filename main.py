import cv2
img =cv2.imread("C:\\Users\\C605\\Desktop\\lab.jpeg")
cv2.imshow('lab' , img)
cv2.waitKey(0)
cv2.desteroyAllWindows()
b = img[:,:,0]
g = img[:,:1]
r = img[:,:,2]
cv2.imshow('la' ,b)
cv2.imshow('l' , g)
cv2.imshow('labb' ,r)
cv2.waitKey(0)
cv2.desteroyAllWindows()