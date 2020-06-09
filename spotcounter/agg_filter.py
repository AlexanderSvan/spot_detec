import scipy.ndimage as ndi
from skimage.measure import regionprops
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import binary_dilation, disk
import math

class agg_analyser:
   
   def __init__(self, intensity, mask, verbose=False):
      self.int_img=intensity
      self.mask=mask
      self.failed_obj=[]
      self.verbose=verbose
      if self.verbose:
         print('Loading spot analyzer')
      
   def find_obj(self, out=False):
      if self.verbose:
         print('Finding bjects')
      self.objects=ndi.label(self.mask)[0]
      self.obj_data=regionprops(self.objects, self.int_img)
      if out==True:
         return self.obj_data
      
   
   def obj_dist(self, attr, bins=20):
      if self.verbose:
         print('Plotting histogram of object {}'.format(attr))
      plt.hist([obj[attr] for obj in self.obj_data], bins)
      plt.show()
      
   def plotting(self, attr, low=0, high=9999):
      passed=[obj.label for obj in self.obj_data if obj[attr]>low and obj[attr]<high]
      canvas=np.isin(self.objects, passed).astype('uint8')
      plt.imshow(self.mask.astype('uint8')+canvas.astype('uint8'))
      plt.show()
      
      

   def filter_obj(self, method=None, **kwargs):
         if self.verbose:
            print('Filtering objects')
         T=self.filters(self)
         if method==None:
            print('No method chosen')
         elif method=='area':
            passed, failed=T.area(**kwargs)
            self.obj_data=passed
         elif method=='round':
            passed, failed=T.roundness(**kwargs)
            self.obj_data=passed
         elif method=='mean_intensity':
            passed, failed=T.mean_int(**kwargs)
            self.obj_data=passed
         for obj in failed:
            self.failed_obj.append(obj)
         
      
   class filters:
      
      def __init__(self, data):
         self.parent_data=data
         self.obj_data=self.parent_data.obj_data
         
      def area(self, low=0, high=9999):
         passed=[]
         failed=[]
         for obj in self.obj_data:
            if obj.area>=low and obj.area<=high:
               passed.append(obj)
            else:
               failed.append(obj)
         return passed, failed
       
      def mean_int(self,low=0, high=9999):
         passed=[]
         failed=[]
         for obj in self.obj_data:
            if obj.mean_intensity>=low and obj.mean_intensity<=high:
               passed.append(obj)
            else:
               failed.append(obj)
         return passed, failed

         
      def roundness(self,low=0.95, high=1.05):
         passed=[]
         failed=[]
         for obj in self.obj_data:
            roundness=obj.area/(obj.major_axis_length/2*obj.minor_axis_length/2*math.pi)
            if roundness>=low and roundness<=high:
               passed.append(obj)
            else:
               failed.append(obj)
         return passed, failed
      
   def plot_filter(self, dilation=None):
      passed_canvas=np.isin(self.objects, [obj.label for obj in self.obj_data]).astype('uint8')
      failed_canvas=np.isin(self.objects, [obj.label for obj in self.failed_obj]).astype('uint8')
            
      overlay=np.zeros_like(self.mask).astype('uint8')
      overlay+=(passed_canvas>0).astype('uint8')
      overlay+=(failed_canvas>0).astype('uint8')*2
      
      if dilation:
         passed_canvas=binary_dilation(passed_canvas, disk(dilation))
         failed_canvas=binary_dilation(failed_canvas, disk(dilation))
         overlay=binary_dilation(binary_dilation, disk(dilation))
         
      passed_canvas=ndi.label(passed_canvas)[0]
      failed_canvas=ndi.label(failed_canvas)[0]
       
      my_cmap = plt.cm.get_cmap('prism')
      my_cmap.set_under('black')
      
      my_cmap2 = plt.cm.get_cmap('bwr',2)
      my_cmap2.set_under('black')
         
      fig2, (ax1,ax2,ax3)=plt.subplots(1,3)
      ax1.set_title('Passed')
      ax1.imshow(passed_canvas, cmap=my_cmap, vmin=1)
      ax1.axis('off')
      ax2.set_title('Failed')
      ax2.imshow(failed_canvas, cmap=my_cmap, vmin=1)
      ax2.axis('off')
      ax3.set_title('Overlaied')
      ax3.imshow(overlay,cmap=my_cmap2, vmin=1)
      ax3.axis('off')
      plt.tight_layout()
      plt.show()
      plt.clf()