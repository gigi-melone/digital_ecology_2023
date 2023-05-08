#!/bin/bash

DATETIME=$(date +"%Y-%m-%d_%H-%M-%S") #Records current date and time with format YYYY-MM-DD_HH-mm-SS

#make directory for files
sudo mkdir -p /mnt/catvid/vids

libcamera-vid --width 4056 --height 3040 --codec mjpeg --save-pts mjpeg -o /mnt/catvid/vids/"$DATETIME".mjpeg --nopreview -t 20000 --framerate 4 --shutter 2500 

echo video recorded!
