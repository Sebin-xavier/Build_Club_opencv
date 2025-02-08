import cv2
path1="tom.jpg"
path2 = "rdj.jpg"
image1=cv2.imread(path1)

image2 = cv2.imread(path2)

h = cv2.hconcat([image1, image2])
g = cv2.hconcat([cv2.cvtColor(i,cv2.COLOR_BGR2GRAY) for i in [image1, image2]])
cv2.imshow("Collage", h)
cv2.imshow("Collage_gray", g)

g=cv2.cvtColor(g, cv2.COLOR_GRAY2BGR)
cv2.imshow("Collage_gray_resized", g)
print(h.shape)

final=cv2.vconcat([h,g])

cv2.imshow("Collage", final)
cv2.imwrite("final.jpg", final)

cv2.waitKey()
cv2.destroyAllWindows()
