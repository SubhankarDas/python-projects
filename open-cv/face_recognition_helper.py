import cv2
import os
import numpy


def read_image_from_path(path):
    # read the image file containing faces and resize it
    img = cv2.imread(path, 1)
    return img


def convert_to_gray(img):
    # convert image to grayscale since classifier works better on grayscale images
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray


def detect_faces(img_gray):
    # create HAAR cascade classifier using the trained cascade XML file from opencv github repo
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # find the faces from the image
    faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

    return faces


def get_faces(img, img_gray, faces):
    faces_array = []
    for (x, y, w, h) in faces:
        # draw a rectangle around all the faces
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        face_img = img_gray[y+1:y+h, x+1:x+w]
        faces_array.append(face_img)

    return img, faces_array


def set_labels(img, label, x, y):
    cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    return img


def get_train_data(directory):
    faces_detected = []
    face_labels = []

    # read files from directories and use directory names as labels
    for path, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(path, file)

            img = read_image_from_path(file_path)
            img_gray = convert_to_gray(img)

            faces = detect_faces(img_gray)
            if(len(faces) > 1):
                print("[", file_path, "] Multiple faces")
            elif(len(faces) < 1):
                print("[", file_path, "] No face found")
            else:
                print("[", file_path, "] Target face found")
                label = os.path.basename(path)
                img, faces_array = get_faces(img, img_gray, faces)
                face = numpy.array(faces_array[0])
                faces_detected.append(face)
                face_labels.append(label)

    return faces_detected, face_labels


def train_image_recognizer(faces, labels):
    print("Training model with face data...")
    img_recognizer = cv2.face.LBPHFaceRecognizer_create()
    img_recognizer.train(faces, labels)

    return img_recognizer


def save_image_recognizer(img_recognizer, name):
    img_recognizer.save(name)


def create_image_recognizer(filename):
    print("Creating image recognizer from file...")
    img_recognizer = cv2.face.LBPHFaceRecognizer_create()
    img_recognizer.read(filename)

    return img_recognizer
