import cv2
import numpy as np

def matrix_gen():
    img_path = "crop.jpeg"
    crop_img = cv2.imread(img_path)

    h, w, channels = crop_img.shape

    height = h//6
    width = w//6

    # mask for red color


    matrix=[]


    for i in range(6):
        curr_height = i*height
        row_matrix=[]
        for j in range(6):
            row_matrix.append(0)
            curr_width = j*width
            part = crop_img[curr_height:curr_height+height,curr_width:curr_width+width]
            hsvFrame = cv2.cvtColor(part, cv2.COLOR_BGR2HSV)
    #        cv2.imshow(str(i)+" "+str(j),part)
    #masking red color
            red_lower = np.array([0, 100, 20], np.uint8)
            red_upper = np.array([10, 255, 255], np.uint8)
     
            red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

            kernal = np.ones((5, 5), "uint8")

            # For red color
            red_mask = cv2.dilate(red_mask, kernal)
            res_red = cv2.bitwise_and(part, part,mask = red_mask)


            contours, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area > 50):
                    row_matrix[-1] = 1
        matrix.append(row_matrix)
    return matrix

