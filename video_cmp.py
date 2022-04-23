#!/bin/env python3

import cv2
import json
import time
import os
import sys
import argparse
import numpy as np

KEY_PAUSE = ord('p')

def process_input(sources, args):
    streams = [cv2.VideoCapture(streamSrc) for streamSrc in sources]

    frameIdx = 0
    while True:
        frames = []
        frameIdx += 1
        for s in streams:
            check, frame = s.read()
            frames.append(frame)
            if not check:
                log("No frames to read")
                return

        print(f"frame #{frameIdx}")
        height, width = frames[0].shape[:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #oframes = []
        delta_frame = cv2.absdiff(frames[0],frames[1])
        #oframes.append(delta_frame)

        cv2.imshow("s1", frames[0])
        cv2.imshow("s2", frames[1])
        cv2.imshow("delta", delta_frame)

        key = cv2.waitKey(1000)
        if key == KEY_PAUSE:
            #wait for unpause
            while cv2.waitKey(1000) != KEY_PAUSE:
                continue

def main():
    parser = argparse.ArgumentParser(description='Compare input video')
    parser.add_argument('input', nargs='+', help="file/rtsp stream")
    args=parser.parse_args()

    cv2.setNumThreads(4)
    process_input(args.input, args)

if __name__ == '__main__':
    main()

