import cv2

import numpy as np
#some basics of open cv

#in opencv images shows as 3d matrix like (300,300,3) 2d pixels and 3 color layers
#and coordinate system starts from top left x +ve to right and y +ve to down


#to load image(show path)
img=cv2.imread('ubuntu wallpaper.jpg')

#img2=cv2.resize(img,(600,300)) # to resize it
#img2=img[0:100,100:200] # to crop in given coordinates

#to make the image b&w do img=cv2.imread('path',0)
#imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # this also make it b&w
#blur=cv2.GaussianBlur(img,(91,91),0) # odd number only(makes image blur)
#blur=cv2.Canny(img,100,100) # detect edges of the image big parameter means more sharp

#import numpy as np # this function dialate pts in the image as the matrix dimensions
#kernal=np.ones((3,3),np.uint8)
#dilated=cv2.dilate(img,kernal,iterations=2)
#if we use erode(inplace of dilate) it is opposite of dilate (ie it shrinks edges)

#this show image for a millisecond
cv2.imshow('wallpaper',img)
#to last the show,0=infinity or the number of milliseconds we are giving
cv2.waitKey(0)

# stacking iamges adjucently
# we can stack numpy array and show it as an image or we can do matplotlib functions but it has limitations when comes
# to videos

hor=np.hstack((img2,img2))
ver=np.vstack((img2,img2))
# this take 2 images of same horizontal (or vertical) dimensions and put them beside each other 
# so if the image is of different dimensions or one b&w other color we have to rescale it both to same shape

#for video
video_capture = cv2.VideoCapture('vidoepath')
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    #now we show each frame as an image
    cv2.imshow('video',frame)
    #the while loop runs forever,to stop it we want a breakpoint,here when we click q it stops the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
#for cam
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    frame=cv2.resize(frame,(48,640))
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # note that this frame is a 480*640*3 pixels,we can change it(crop) or add simple filters to it to make the
    # video any changes like
    # frame=frame[:280]
    # or we can do resize function as given to sqeeze the camera ond crop video

#shapes

#create a blank image
img=np.zeros((400,400,3),np.uint8)
#to make a rectangle of desitred color
img[20:40,40:50]=240,100,10
#to change whole color
img[:,:]=200,100,10
#to draw shapes
cv2.line(img,(10,20),(102,202),(100,260,23),9)
# we do this and rectangle this format
cv2.circle(img,(200,200),100,(200,100,100),cv2.FILLED)
#cv2.shape(image,(x1,x2),(y1,y2),(color1,color2,color3),thickness)
#to put text
cv2.putText(img,'this is text',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(100,100,200),2)

# like this we can draw over vidoes also




