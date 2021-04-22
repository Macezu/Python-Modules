import cv2

img = cv2.imread("resources/Ennen.PNG")

imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imggray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny,)


cv2.imshow("BlurImg",imgblur)
cv2.imshow("GrayImg",imggray)
cv2.imshow("Canny",imgCanny)
cv2.waitKey(0)