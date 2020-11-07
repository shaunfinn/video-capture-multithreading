# import the necessary package
from __future__ import print_function

import cv2
import imutils
import argparse
from imutil import FPS
from imutil import WebCamVideoStream

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--num-frames", type=int, default=100,
            help="# of frames to loop over FPS test")
    ap.add_argument("-d", "--display", type=int, default=-1,
            help="whether or not frames should be displayed")
    ap.add_argument("-w", "--write", type=bool, default=False,
                    help="whether or not frames should be displayed")
    args = vars(ap.parse_args())

    # grab a pointer to the video stream and initialize the FPS counter
    print ("[INFO] sampling frames from webcam")
    stream = cv2.VideoCapture(0)

    #set to max resolution and get
    stream.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
    stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)
    width = int(stream.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(stream.get(cv2.CAP_PROP_FRAME_HEIGHT))
    res = (width, height)

    write = args["write"]
    if write:
        fourcc = cv2.VideoWriter_fourcc(*'FFV1')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, res)


    fps = FPS().start()

    # loop over some frames
    while fps._numFrames < args["num_frames"]:
        # grab the frame from the stream and resize it to have a maximum 
        # width of 400 pixels
        (grabbed, frame) = stream.read()

        # check to see if the frame should be displayed on screen
        if args["display"] > 0:
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xff
        if write:
            out.write(frame)

        # update the fps counter
        fps.update()

    # stop the timer and display the information
    fps.stop()
    print ("[INFO] elapsed time : {:.2f}".format(fps.elapsed()))
    print ("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
    stream.release()




