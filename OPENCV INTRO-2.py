import cv2

import numpy as np

# BIRDVIEW-we can make 3d images look like 2d or vice versa like top view or as pdfscanner
# change paper to a rectangele
# here we are taking a polygonal part from the image and making it a square

img=cv2.imread('ubuntu wallpaper.jpg')
cv2.circle(img,(660,340),4,(100,100,200),cv2.FILLED)
cv2.circle(img,(880,340),4,(100,100,200),cv2.FILLED)
cv2.circle(img,(730,540),4,(100,100,200),cv2.FILLED)
cv2.circle(img,(840,540),4,(100,100,200),cv2.FILLED)

# pts1,pts2=coordinates we want to change,coordinates to where we want to change it

pts1=np.float32([[660,340],[880,340],[730,540],[840,540]])
pts2=np.float32([[0,0], [0,200], [200,0], [200,200]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
newimg=cv2.warpPerspective(img,matrix,(200,200))


cv2.imshow('wallpaper',newimg)
cv2.waitKey(0)

#using mousepoint for different purposes
#here we define a function ie if we did left button click it executes
def mousepoints(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        print (x,y)

cv2.imshow('wallpaper',img)
#then we call this function that says do mousepoints function on wallpaper named image
#we can do lots of applications on this thing
cv2.setMouseCallback('wallpaper',mousepoints)
cv2.waitKey(0)




