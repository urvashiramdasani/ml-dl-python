# Develop a python program which takes the video
# as an argument and extract all the frames from 
# a video. Select specific frames and recreate 
# the video, which has selected frames only.

import cv2

vid = cv2.VideoCapture('video.mp4')
if vid.isOpened() == False:
  print('Error in playing video!')

ret, frame = vid.read() # returns a tuple (return value, frame). If reading was successful, return value is True
height, width, layers = frame.shape
new_vid = cv2.VideoWriter('New_Video.mp4',-1,1,(width, height))
count = 0

while(vid.isOpened()):
  ret, frame = vid.read()
  count+=1
  if ret:

  	# taking selected frames only
  	if count%4 == 0:
  		new_vid.write(frame)
  else:
  	break

print('New Video successfully exported!')

# Note : The difference is observed by breaks between frames in the New_video