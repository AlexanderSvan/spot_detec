import cv2
import numpy as np

def slide_filter(objects, attr, scale=1):
   def nothing(x):
      pass
    
   def normalize(f):
      lmin = float(f.min())
      lmax = float(f.max())
      return np.floor((f-lmin)/(lmax-lmin)*255).astype('uint8')     
   
   def obj2attr_img(objects, attr):
      labels=objects[0]._label_image
      canvas=np.zeros_like(labels)
      for obj in objects:
         canvas[labels==obj.label]=obj[attr]
      return canvas

   int_img=objects[0]._intensity_image
   int_img=normalize(cv2.resize(int_img, (0,0), fx=scale, fy=scale)).astype('uint8')
   
   obj2img=obj2attr_img(objects, attr)
   attr_max=np.amax(obj2img)
   inpimg=normalize(obj2img).astype('uint8')
   
   cv2.namedWindow('image')

   imgOri=cv2.resize(inpimg, (0,0), fx=scale, fy=scale)

   img=imgOri
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
           imgSwap = int_img
       else:
           imgSwap = (imgOri>r).astype('uint8')*255
   
   cv2.destroyAllWindows()
   return int(attr_max*r/255)

if __name__ =='__main__':
   print(slide_filter(objects, 'max_intensity', scale=0.3))
