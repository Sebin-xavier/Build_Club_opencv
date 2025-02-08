import cv2
import cv2.videoio_registry

cam = cv2.VideoCapture(0)

print(cam.get(cv2.CAP_PROP_FPS))
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280 ) 
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720 ) 
cam.set(cv2.CAP_PROP_FPS, 2 )
output_path = "recording.mp4"
output = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MJPG'), 20, (1280, 720))
while True:
    _, frame = cam.read()
    cv2.imshow("Webcam", frame)
    output.write(frame)
    if cv2.waitKey(1)& 0xff == ord('q'):# 64 and 32 bit compatability 0xff
        break

print(cam.get(cv2.CAP_PROP_GAMMA))    
cam.release()
output.release()
cv2.destroyAllWindows()