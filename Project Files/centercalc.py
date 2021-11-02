#return image and list of centroids
#input black and white and original image
import cv2
import numpy as np;

# Read image
def calculatecenters(im,orig):
    # im = cv2.imread("inter.jpg", cv2.IMREAD_GRAYSCALE)
    # orig = cv2.imread("checks.jpg")
    ret,binary = cv2.threshold(im,127,255,0)


    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # draw all contours
    print(len(contours))
    image = cv2.drawContours(orig, contours, -1, (0, 255, 0), 2)
    cv2.imshow("he",cv2.resize(image,(500,500)))
    cv2.waitKey(0)
    counter = 0
    centers = []
    for c in contours:
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            counter+=1
        else:
            cX,cY = 0,0
        centers.append((cX,cY))
        print(cX,cY)
        cv2.circle(orig, (cX, cY), 5, (255, 255, 255), -1)
        cv2.putText(orig, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.imshow("he",cv2.resize(orig,(500,500)))
    return centers,orig
    cv2.waitKey(0)

# Set up the detector with default parameters.
# im=cv2.bitwise_not(im)

# params = cv2.SimpleBlobDetector_Params()
# detector = cv2.SimpleBlobDetector_create(params)


# # Detect blobs.
# keypoints = detector.detect(im)
# im=cv2.bitwise_not(im)
# # Draw detected blobs as red circles.
# # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
# im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# print(keypoints)
# # Show keypoints
# cv2.imshow("Keypoints", cv2.resize(im_with_keypoints,(500,500)))
# cv2.waitKey(0)