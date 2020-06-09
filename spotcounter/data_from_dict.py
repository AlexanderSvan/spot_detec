import pandas as pd
import numpy as np
import ast

def dict2df(dict_in=None, layout=None):
   with open(dict_in, 'r') as file:
           data=ast.literal_eval(file.read())
   
   df=pd.DataFrame.from_dict({(i,j): data[i][j] 
                              for i in data.keys() 
                              for j in data[i].keys()},
                          orient='index')
   
   df=df.reset_index()
   df.columns=['well', 'timepoint','cell_area','agg_count','mean_agg_size','total_agg_area','mean_int', 'total_int','um^2_agg/um^2_cell']

   condition_names=[param[0] for param in layout]
   condition_paths=tuple(np.loadtxt(param[1], delimiter=";", dtype=str).ravel() for param in layout)
   conditions = pd.DataFrame(np.vstack(condition_paths).T, 
                     columns=condition_names)
   
   conditions['well'].astype(str)
   df['well']=df['well'].astype(str)
   
   return conditions.merge(df,on='well')

if __name__ =='__main__':

   layout=[['well','/media/data/Jan/20191205 - ONE-HNE/Numbering.csv'],
           ['oligo','/media/data/Jan/20191205 - ONE-HNE/ONE-HNE-1.csv'],
           ['oligo_type','/media/data/Jan/20191205 - ONE-HNE/Oligo_type.csv'],
           ['PFF','/media/data/Jan/20191205 - ONE-HNE/PFF.csv']]
      
   df=dict2df(dict_in='/media/data/Jan/20191205 - ONE-HNE/results.txt',layout=layout)
      
