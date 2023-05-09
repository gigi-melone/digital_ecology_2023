#import modules
import numpy as np
import cv2
import csv
import os


# Define the folder path containing the videos
folder_path = '/media/bombus/7A61FA006E6AE2B1/vids/april10_control2'

#model for background subtraction
backSub = cv2.createBackgroundSubtractorMOG2()

# Define the output CSV file path
csv_file_path = '/media/bombus/7A61FA006E6AE2B1/output.csv'

# Open the CSV file for writing
with open(csv_file_path, 'w') as csv_file:
    # Write the header row to the CSV file
    csv_file.write('frame_number,object_id,x,y\n')

    # Loop through the video files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.mjpeg'):
            # Open the video file
            cap = cv2.VideoCapture(os.path.join(folder_path, filename))
            frame_number = 0

            #loop through frames in video 
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break


                #Perform blob tracking on the frame here
                #Create mask of moving objects
                fgMask = backSub.apply(frame)
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
                fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_OPEN, kernel)
                fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_CLOSE, kernel)
                contours, hierarchy = cv2.findContours(fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
                # Draw the contours on the original frame
                frame_contours = frame.copy()
                
                # Find the centroids of the contours and draw them on the frame
                for object_id, cnt in enumerate(contours):
                    M = cv2.moments(cnt)
                    if M["m00"] != 0 and cv2.contourArea(cnt) > 50 and cv2.contourArea(cnt) < 5000:
                        cx = int(M["m10"] / M["m00"])
                        cy = int(M["m01"] / M["m00"])
                        cv2.circle(frame_contours, (cx, cy), 5, (0, 0, 255), -1)
                        cv2.drawContours(frame, [cnt], 0, (0,255,0), 3)
                        print(cnt)
                        # Write the centroid coordinates to the CSV file
                        csv_file.write(f'{frame_number},{object_id},{cx},{cy}\n')
                frame_number = frame_number + 1
                # Display the frames
                #cv2.imshow("Frame", frame)
                #cv2.imshow("Foreground Mask", fgMask)
                cv2.imshow("Contours", cv2.resize(frame_contours, None, fx=0.25, fy=0.25))

        
                #cv2.imshow("Frame", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

cap.release()
cv2.destroyAllWindows()
