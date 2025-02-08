import cv2
import numpy as np
import time
image = cv2.imread("tom.jpg")
cv2.imshow("Image", image)

image.resize(400, 400, 3)
print(image.shape)
width,height,channel=image.shape
check = 0
for i in range(4):
    for j in range(4):
        if check == 0:
            image[i*width//4:(i+1)*width//4,j*height//4:(j+1)*height//4]=255
            check = 1
        else:
            image[i*width//4:(i+1)*width//4,j*height//4:(j+1)*height//4]=0
            check = 0
    check = 0 if check == 1 else 1
        

output = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'MJPG'), 1, (400, 400))

while True:
    output.write(image)
    output.write(cv2.bitwise_not(image))
    
    time.sleep(1.0)
    
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cv2.imshow("Image", image)

cv2.waitKey()
cv2.destroyAllWindows()