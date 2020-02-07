import cv2

# open video capture using default camera(0)
video = cv2.VideoCapture(0)

# create cascade classifier from XML file
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

frame_count = 0

while True:
    frame_count += 1
    read, frame = video.read()  # read the current image frame

    # convert image to grayscale and detect faces
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.1, 7)

    # draw rectangles over faces into image frame
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # display the captured image
    cv2.imshow("Capturing...", frame)

    # wait for 1 milliseconds to capture key input, if Q is pressed or unable to read data break loop
    key = cv2.waitKey(1)
    if (key == ord('q') or not read):
        break

print("Total no. of frames captured:", frame_count)

# close video capture and close all windows
video.release()
cv2.destroyAllWindows()
