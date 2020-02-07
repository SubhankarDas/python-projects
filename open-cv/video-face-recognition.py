import cv2
import face_recognition_helper as fr
import numpy

faces_dict = {"subhankar": 0, "deepayan": 1,
              "chayan": 2, "ajit": 3, "deepa": 4, "sankar": 5, "sayan": 6}
names = {0: "subhankar", 1: "deepayan",
         2: "chayan", 3: "ajit", 4: "deepa", 5: "sankar", 6: "sayan"}

# get faces data with labels
faces, labels = fr.get_train_data("images/train-images")

lan = []
for l in labels:
    lan.append(faces_dict[l])


# uncomment below lines to train the model and save as XML file
# img_recognizer = fr.train_image_recognizer(faces, numpy.array(lan))
# fr.save_image_recognizer(img_recognizer, "friends-family-faces.xml")

img_recognizer = fr.create_image_recognizer("friends-family-faces.xml")

video = cv2.VideoCapture(0)

while True:
    read, img = video.read()  # read image frame
    img_gray = fr.convert_to_gray(img)

    faces = fr.detect_faces(img_gray)  # detect faces

    img, faces_array = fr.get_faces(img, img_gray, faces)  # get faces array

    idx = 0
    for face in faces_array:
        label, confidence = img_recognizer.predict(face)
        lbl = names[label] + "[" + str(int(confidence))+"]"
        x = faces[idx][0]
        y = faces[idx][1]
        if (confidence < 50):
            img = fr.set_labels(img, lbl, x, y-5)

        idx += 1

    cv2.imshow("Detected", img)

    key = cv2.waitKey(1)
    if (key == ord('q') or not read):  # break loop on Q key press
        break

# destroy all windows
video.release()
cv2.destroyAllWindows()
