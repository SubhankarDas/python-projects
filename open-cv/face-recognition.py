import cv2
import face_recognition_helper as fr
import numpy

faces_dict = {"subhankar": 0, "deepayan": 1,
              "chayan": 2, "ajit": 3, "deepa": 4, "sankar": 5, "sayan": 6}
names = {0: "subhankar", 1: "deepayan",
         2: "chayan", 3: "ajit", 4: "deepa", 5: "sankar", 6: "sayan"}


faces, labels = fr.get_train_data("images/train-images")

# create labels array corresponsing to names
lan = []
for l in labels:
    lan.append(faces_dict[l])

# train model with faces data and corresponding labels
img_recognizer = fr.train_image_recognizer(faces, numpy.array(lan))

# read image and convert to gray scale
img = fr.read_image_from_path("images/test-images/faces.jpg")
img_gray = fr.convert_to_gray(img)

# detect faces and get face coordinates
faces = fr.detect_faces(img_gray)
img, faces_array = fr.get_faces(img, img_gray, faces)

# predict faces labels and confidence score
idx = 0
for face in faces_array:
    label, confidence = img_recognizer.predict(face)
    lbl = names[label] + "[" + str(int(confidence))+"]"
    x = faces[idx][0]
    y = faces[idx][1]
    if (confidence < 70):
        img = fr.set_labels(img, lbl, x, y-5)

    idx += 1

# show labeled image
cv2.imshow("Detected", img)

print("Detected Faces:", len(faces))

# wait for any key press and then destroy opened windows
cv2.waitKey(0)
cv2.destroyAllWindows()
