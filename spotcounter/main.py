import nd2reader as nd2
from .sliding_thresh import threshold
from .agg_filter import agg_analyser
import numpy as np
import time
import json
from .visual_filtering import slide_filter
import os

class timelaps_agg:
   """Analyses an ND2 timelaps for spots and normalizes to seconday objects.
   
   """
   
   def __init__(self,path):
      self.loader(path)
      self.cwd=os.path.dirname(path)
      self.cell_thresh=None
      self.agg_thresh=None
      self.filters={}
      
   def set_freq(self, freq):
      self.freq=freq
      
   def loader(self, path):
      self.src=nd2.ND2Reader(path)
      self.src.bundle_axes='yx'
      self.src.default_coords['v'] = 7
      self.src.iter_axes='t'
      self.px_size=self.src.metadata['pixel_microns']
      self.px_area=self.px_size**2
   
   def set_cellthresh(self, **kwargs):
      self.cell_thresh=threshold(self.src[96], **kwargs)
   
   def set_aggthresh(self, **kwargs):
      self.agg_thresh=threshold(self.src[96], **kwargs)
   
   def obj_dist(self, attr, bins=20,**kwargs):
      img=self.src[90]
      mask=img>self.agg_thresh
      t=agg_analyser(img, mask)
      t.find_obj()
      t.obj_dist(attr, bins=bins)
      
   def set_filters(self, attr,**kwargs):
      low=self.visual_filter(attr, **kwargs)
      high=self.visual_filter(attr, **kwargs)
      cutoff={'high':high, 'low': low}
      self.filters[attr]=cutoff
      
   def visual_filter(self, attr, **kwargs):
      img=self.src[90]
      mask=img>self.agg_thresh
      t=agg_analyser(img, mask)
      objects=t.find_obj(out=True)
      return slide_filter(objects, attr, **kwargs)
   
   def run_analysis(self):
      def count_agg(self, img,i):
         cell_area=np.count_nonzero(img>self.cell_thresh)*self.px_area
         mask=img>self.agg_thresh
         t=agg_analyser(img, mask)
         t.find_obj()
         for filter in self.filters:
            t.filter_obj(filter,**self.filters[filter])
         if len(t.obj_data)>1:
            mean_agg=(sum([a.area for a in t.obj_data])/len(t.obj_data))*self.px_area
            mean_int=sum([a.mean_intensity for a in t.obj_data])/len(t.obj_data)
            total_int=sum([a.mean_intensity*a.area for a in t.obj_data])/len(t.obj_data)
            agg_count=len(t.obj_data)
            total_agg_area=(len(t.obj_data)*mean_agg)*self.px_area
         else:
            mean_agg=0
            mean_int=0
            total_int=0
            agg_count=0
            total_agg_area=0
         return {'cell_area': cell_area,
                 'agg_count': agg_count,
                 'mean_agg_size': mean_agg,
                 'total_agg_area': total_agg_area,
                 'mean_int': mean_int,
                 'total_int': total_int,
                 'um^2_agg/um^2_cell':total_agg_area/cell_area}

      start=time.time()
      self.results={}
      for well in range(self.src.sizes['v']):
         lap=time.time()
         self.src.default_coords['v'] = well
         self.results[well]={}
         for i,img in enumerate(self.src):
            self.results[well][i*self.freq]=count_agg(self,img,i)
         print(time.time()-lap)
         print(str(well+1)+"/"+str(self.src.sizes['v'])+ " wells")
      print("finished in "+str(time.time()-start)+" seconds")
   
   def save(self):
      with open(self.cwd+"/results.txt", 'w') as outfile:
          json.dump(self.results, outfile)
   
if __name__ == '__main__':
   a=timelaps_agg('/media/data/Jan/20191205 - ONE-HNE/Oligo002.nd2')
   a.set_freq(0.5)
   a.set_cellthresh(scale=0.3)
   a.set_aggthresh(scale=0.3)
   a.set_filters('area', scale=0.3)
   a.run_analysis()
   a.save()