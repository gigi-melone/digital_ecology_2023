#!/bin/bash


#DATE=$(date +"%Y-%m-%d") #This record the current date with format YYYY-MM-DD
#echo $DATE
DATETIME=$(date +"%Y-%m-%d_%H-%M-%S") #Records current date and time with format YYYY-MM-DD_HH-mm-SS
#OUTPUT= /mnt/catvid/"$HOSTNAME"_"$DATE"/"$HOSTNAME"_"$DATETIME".mjpeg

#OUTPUT=/mnt/catvid/"$HOSTNAME"_"$DATE"/"$HOSTNAME"_"$DATETIME".mpeg
#OUTPUT="$VIDEO_DIRECTORY"/"$HOSTNAME"_"$DATE"/"$HOSTNAME"_"$DATETIME"."$CODEC"

#sudo mkdir -p /mnt/catvid/"$HOSTNAME"_"$DATE"
#sudo mkdir -p /mnt/catvid/"$HOSTNAME"_"$DATE"
#echo $OUTPUT

#libcamera-vid --width 4056 --height 3040 --codec mjpeg --save-pts mjpeg -o "$OUTPUT" --nopreview -t 20000 --framerate 4 --shutter 2500 
libcamera-vid --width 4056 --height 3040 --codec mjpeg --save-pts mjpeg -o /mnt/catvid/vids/"$DATETIME".mjpeg --nopreview -t 20000 --framerate 4 --shutter 2500 

echo video recorded!
