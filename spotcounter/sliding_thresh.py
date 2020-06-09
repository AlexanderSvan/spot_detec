import cv2
import numpy as np

def threshold(inpimg, scale=1):
   def nothing(x):
      pass
    
   def normalize(f):
      lmin = float(f.min())
      lmax = float(f.max())
      return np.floor((f-lmin)/(lmax-lmin)*255).astype('uint8')     
   
   # Create a black image, a window
   # imgOri = inpimg
   cv2.namedWindow('image')
   # img=imgOri
   imgOri=cv2.resize(inpimg, (0,0), fx=scale, fy=scale)
   
   img=normalize(imgOri)
   max=int(np.amax(inpimg))
   # create trackbars for color change
   cv2.createTrackbar('Threshold','image',0,max,nothing)
   
   toggle=True
   
   imgSwap=img
   
   while(1):
       cv2.imshow('image',imgSwap)
       k = cv2.waitKey(1) & 0xFF
       if k == 27:
           break
       if k == 32:
          toggle=np.invert(toggle)
   
       # get current positions of four trackbars
       r = cv2.getTrackbarPos('Threshold','image')
       
       if toggle == True:
           imgSwap = img
       else:
           imgSwap = (imgOri>r).astype('uint8')*255
   
   cv2.destroyAllWindows()
   return r
