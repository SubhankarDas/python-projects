import cv2

# read the image file containing faces and resize it
img = cv2.imread("images/test-images/face.jpg", 1)
img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# convert image to grayscale since classifier works better on grayscale images
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# display original and grayscale image
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", img_gray)

# create HAAR cascade classifier using the trained cascade XML file from opencv github repo
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# find the faces from the image
faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

# draw a rectangle around all the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# show the detected faces
cv2.imshow("Detected", img)

print("No. of detected faces:", len(faces))

# wait for any key press and then destroy opened windows
cv2.waitKey(0)
cv2.destroyAllWindows()
