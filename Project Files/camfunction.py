import cv2
import numpy as np
from PIL import Image 
from centercalc import *
img = cv2.imread('legmini.jpg')
# img = cv2.imread('checks.JPG')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Keypoints", cv2.resize(hsv,(500,500)))
cv2.waitKey(0)
# color_ranges = {"yellow":[[20, 90, 100],[50, 255, 255]], "red":[[0,50,50],[10,255,255],[170,50,50],[180,255,255]], "green":[[25, 52, 72],[102, 255, 255]]}
color_ranges = {"yellow":[[20, 110, 100],[50, 255, 255]], "red":[[0,70,70],[2,255,255],[170,50,50],[180,255,255]], "green":[[30, 60, 60],[120, 255, 255]]}
#[[0,50,50],[10,255,255],[170,50,50],[180,255,255]]
#[[155,25,0],[179,255,255]]
def imshow(img):
    cv2.imshow("image",cv2.resize(img,(500,500)))
def colormask(color):
    number = len(color_ranges[color])
    mask_lower = np.array(color_ranges[color][0])
    mask_upper = np.array(color_ranges[color][1])
    mask = cv2.inRange(hsv, mask_lower, mask_upper)
    imshow(mask)
    cv2.waitKey(0)
    # exit()
    if(number>2):
        mask_lower = np.array(color_ranges[color][2])
        mask_upper = np.array(color_ranges[color][3])
        mask = mask + cv2.inRange(hsv, mask_lower, mask_upper)
        imshow(mask)
        cv2.waitKey(0)
    output = cv2.bitwise_and(img, img, mask=mask)
    imshow(output)
    cv2.waitKey(0)
    gray_image = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    ret, frame = cv2.threshold(gray_image,10,255,cv2.THRESH_BINARY)
    imshow(frame)
    cv2.waitKey(0)
    # exit()
    kernel = np.ones((25,25),np.uint8)
    frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
    frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
    imshow(frame)
    cv2.waitKey(0)
    # exit()
    return frame



# yellow_lower = np.array([20, 90, 100])
# yellow_upper = np.array([50, 255, 255])



# frame = cv2.erode(frame,kernel,iterations = 15)
# frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)

# frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
# frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
def act():
    possible = {"red","green"}
    returncenters = []
    for co in  color_ranges:
        if not co in possible:
            continue
        
        fr = colormask(co)
        allcenters,newimg = calculatecenters(fr,img )
        print(allcenters)
        returncenters.append(allcenters)
        imshow(newimg)
        cv2.waitKey(0)
    return returncenters


