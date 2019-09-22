import cv2
import time
import os
from datetime import datetime

# creating a video object using default cam
video = cv2.VideoCapture(0)

# max number of frames to capture
nframes = 10

# capture every 5 seconds
interval = 5

folder = "pictures/"

os.mkdir(folder)

a = 0
while a < nframes:
    a = a + 1
    # create a frame object
    check, frame = video.read()

    # display the frame
    cv2.imshow("Capturing", frame)

    # save frame with timestamp as name
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%y%m%d%H%M%S")

    cv2.imwrite(folder + "file%s.jpg" % (timestampStr), frame)
    time.sleep(interval)

    # q key pressed ?
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
