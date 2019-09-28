import cv2
import time
import os
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-w', type=int, default=0,
                    help="the number of the webcam device")
parser.add_argument('-c', type=int, default=0,
                    help="number of frames to capture. Default is forever")
args = parser.parse_args()
cam = args.w


# creating a video object using default cam
video = cv2.VideoCapture(cam)

# max number of frames to capture
nframes = args.c

# capture every 5 seconds
interval = 5

folder = "pictures/"

if not os.path.exists(folder):
    os.makedirs(folder)

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
