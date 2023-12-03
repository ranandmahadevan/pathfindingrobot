import cv2
import numpy as np

def photo():  
    cam = cv2.VideoCapture(1)
    
    # reading the input using the camera
    result, image = cam.read()

    #select ROI function
    roi = cv2.selectROI(image)

    #print rectangle points of selected roi
    print(roi)

    #Crop selected roi from raw image
    roi_cropped = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    #show cropped image
    cv2.imshow("ROI", roi_cropped)

    cv2.imwrite("crop.jpeg",roi_cropped)

    #hold window
    cv2.waitKey(0)
 
photo()