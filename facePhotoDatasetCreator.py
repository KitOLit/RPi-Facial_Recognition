#! /usr/bin/python

import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

name = " " #Enter the Name of the person of whom photos would be clicked.

camera = PiCamera()
camera.resolution = (512, 304)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size = camera.resolution)
photoCounter = 0

while True:
    for frame in camera.capture_continuous(rawCapture, format = "bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Press spacebar to click photos", image)
        rawCapture.truncate(0)

        wait_key = cv2.waitKey(1)
        rawCapture.truncate(0)
        if wait_key&256 == 27:
            # ESC Key pressed
            break
        elif wait_key%256 == 32:
            # SPACE BAR pressed
            image_name = f"Dataset/{name}" + f"/image_{photoCounter}.jpg"
            cv2.imwrite(image_name, image)
            print(f"{image_name} written!")
            photoCounter += 1
    if wait_key%256 == 27:
        print("Escape hit, closing...")
        break

cv2.destroyAllWindows()