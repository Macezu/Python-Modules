import cv2
print("Package imported")
img = cv2.VideoCapture(0)
img.set(3, 640)
img.set(4, 480)
img.set(10, 500)

while True:
    success, feed = img.read()
    cv2.imshow("Feed", feed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break