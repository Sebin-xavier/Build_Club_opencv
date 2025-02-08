import cv2
import numpy as np
image = cv2.imread("tom.jpg")
cv2.imshow("Image", image)
B = image[:,:,0]
G = image[:,:,1]
R = image[:,:,2]
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)    

B=B+100
G=G+100
R=R+100

        
        
image_merged = cv2.merge((B, G, R)) 
cv2.imshow("Image_merged", image_merged)
cv2.waitKey()
cv2.destroyAllWindows()