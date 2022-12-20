import cv2
import imutils
import numpy as np
import argparse

def detect(frame):
    bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)
    
    person = 1
    for x,y,w,h in bounding_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, 'person: {}'.format(person), (x,y), cv2.FONT_ITALIC, 0.6, (0,255,0), 1)
        person += 1
    
    cv2.putText(frame, 'Outcome: {}'.format(person-1), (20,30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 2)
    cv2.imshow('Person detection', frame)

    return frame


def detectByPathImage(path, output_path):
    image = cv2.imread(path)

    image = imutils.resize(image, width = min(800, image.shape[1]))

    result_image = detect(image)

    if output_path is not None:
        cv2.imwrite(output_path, result_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def humanDetector(args):
    image_path = args["image"]


def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-i", "--image", default=None, help="1.jpeg ")
    args = vars(arg_parse.parse_args())
    return args


if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    detectByPathImage("9.jpeg","count.jpeg")