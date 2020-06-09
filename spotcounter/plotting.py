from data_from_dict import dict2df
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

layout=[['well','/media/data/Jan/20191205 - ONE-HNE/Numbering.csv'],
        ['oligo','/media/data/Jan/20191205 - ONE-HNE/ONE-HNE-1.csv'],
        ['oligo_type','/media/data/Jan/20191205 - ONE-HNE/Oligo_type.csv'],
        ['PFF','/media/data/Jan/20191205 - ONE-HNE/PFF.csv']]
   
df=dict2df(dict_in='/media/data/Jan/20191205 - ONE-HNE/results.txt',layout=layout)
df['timepoint']=df['timepoint'].astype(float)

df2=df.groupby(['well', 'oligo','oligo_type', 'PFF','timepoint']).mean()

df2=df2.reset_index()

#%% 1 PFF various ONE
legends=[]
for v in [7,16,31,40]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='total_agg_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('aggregates/field \n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Aggregate area | 1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% 0.1 PFF various ONE
legends=[]
for v in [5,18,29,42]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='total_agg_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('aggregates/field \n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Aggregate area | 0.1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% 0.01 PFF various ONE
legends=[]
for v in [3,20,27,44]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='total_agg_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('aggregates/field \n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Aggregate area | 0.01 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% 0.001 PFF various ONE
legends=[]
for v in [1,22,25,46]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='total_agg_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('aggregates/field \n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Aggregate area | 0.001 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()

#%% Viability 1 PFF various ONE
legends=[]
for v in [7,16,31,40]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='cell_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('cell coverage\n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Cell density | 1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% Viability 0.1 PFF various ONE
legends=[]
for v in [5,18,29,42]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='cell_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('cell coverage\n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Cell density | 0.1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% Viability 0.01 PFF various ONE
legends=[]
for v in [3,20,27,44]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='cell_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('cell coverage \n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Cell density | 0.01 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% Viability 0.001 PFF various ONE
legends=[]
for v in [1,22,25,46]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='cell_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('cell coverage\n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Cell density | 0.001 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% norm 1 PFF various ONE
legends=[]
for v in [7,16,31,40]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y=well.columns[-1], data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0,0.0035))
plt.ylabel('aggregate area/ \n cell area')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Normalized agg. area | 1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% norm 0.1 PFF various ONE
legends=[]
for v in [5,18,29,42]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y=well.columns[-1], data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0,0.00035))
plt.ylabel('aggregate area/ \n cell area')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Normalized agg. area | 0.1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% norm 0.01 PFF various ONE
legends=[]
for v in [3,20,27,44]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y=well.columns[-1], data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0,0.00035))
plt.ylabel('aggregate area/ \n cell area')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Normalized agg. area | 0.01 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% norm 0.001 PFF various ONE
legends=[]
for v in [1,22,25,46]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y=well.columns[-1], data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0,0.00035))
plt.ylabel('aggregate area/ \n cell area')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Normalized agg. area | 0.001 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()

#%% 1 PFF various HNE
legends=[]
for v in [55,62,77,84]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='total_agg_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('aggregates/field \n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Aggregate area | 1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% 0.1 PFF various HNE
legends=[]
for v in [53,64,75,86]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='total_agg_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('aggregates/field \n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Aggregate area | 0.1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% 0.01 PFF various HNE
legends=[]
for v in [51,66,73,88]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='total_agg_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('aggregates/field \n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Aggregate area | 0.01 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% 0.001 PFF various HNE
legends=[]
for v in [49,68,71,90]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='total_agg_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('aggregates/field \n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Aggregate area | 0.001 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()

#%% Viability 1 PFF various HNE
legends=[]
for v in [55,62,77,84]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='cell_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('cell coverage\n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Cell density | 1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% Viability 0.1 PFF various HNE
legends=[]
for v in [53,64,75,86]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='cell_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('cell coverage\n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Cell density | 0.1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% Viability 0.01 PFF various HNE
legends=[]
for v in [51,66,73,88]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='cell_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('cell coverage\n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Cell density | 0.01 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% Viability 0.001 PFF various HNE
legends=[]
for v in [49,68,71,90]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y='cell_area', data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0))
plt.ylabel('cell coverage\n($um^2$)')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Cell density | 0.001 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% norm 1 PFF various HNE
legends=[]
for v in [55,62,77,84]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y=well.columns[-1], data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0,0.0035))
plt.ylabel('aggregate area/ \n cell area')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Normalized agg. area | 1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% norm 0.1 PFF various HNE
legends=[]
for v in [53,64,75,86]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y=well.columns[-1], data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0,0.00035))
plt.ylabel('aggregate area/ \n cell area')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Normalized agg. area | 0.1 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% norm 0.01 PFF various HNE
legends=[]
for v in [51,66,73,88]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y=well.columns[-1], data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0,0.00035))
plt.ylabel('aggregate area/ \n cell area')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Normalized agg. area | 0.01 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% norm 0.001 PFF various HNE
legends=[]
for v in [49,68,71,90]:
   well=df2[df2['well']==str(v)]
   r=sns.regplot(x="timepoint", y=well.columns[-1], data=well,
                  scatter_kws={"s": 10},
                 order=3, ci=None)
   legends.append(well.iloc[0]['oligo']+" "+well.iloc[0]['oligo_type']+"/"+well.iloc[0]['PFF']+" PFF")
r.spines['right'].set_visible(False)
r.spines['top'].set_visible(False)
r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5))

plt.xlim((0,48))
plt.ylim((0,0.00035))
plt.ylabel('aggregate area/ \n cell area')
plt.xlabel('duration \n ($hours$)')
plt.title(r'Normalized agg. area | 0.001 $\frac{ug}{ml}$ PFF', size=20)
plt.show()
plt.clf()
#%% Graph generator - fixed PFF
def graph(samples, condition,ylab,save_name):
   legends=[]
   y_max=0
   for v in samples:
      well=df2[df2['well']==str(v)]
      start=list(well[well['timepoint']==0]['cell_area'])
      well['cell_area_norm']=(well['cell_area']/start)*100
      if y_max< np.amax(well[condition]):
         y_max=np.amax(well[condition])
      r=sns.regplot(x="timepoint", y=condition, data=well,
                    scatter_kws={"s": 10},
                    order=3, ci=None)
      legends.append(well.iloc[0]['oligo']+r" $\frac{ug}{ml}$ "+well.iloc[0]['oligo_type']+" / "+well.iloc[0]['PFF']+r" $\frac{ug}{ml}$ PFF")
   r.spines['right'].set_visible(False)
   r.spines['top'].set_visible(False)
   r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5),prop={'size': 8})
   
   plt.xlim((0,49))
   plt.ylim((0, y_max*1.1))
   plt.ylabel(ylab)
   plt.xlabel('duration \n ($hours$)')
   # plt.title(title, size=20)
   plt.tight_layout()
   plt.savefig(save_name+".png", dpi=300, figsize=(20,10))
   plt.show()
   plt.clf()
   
samples=[([49,68,71,90],'0_PFF','HNE'),
         ([51,66,73,88],'0.01_PFF','HNE'),
         ([53,64,75,86],'0.1_PFF','HNE'),
         ([55,62,77,84],'1_PFF','HNE'),
         ([1,22,25,46],'0_PFF','ONE'),
         ([3,20,27,44],'0.01_PFF','ONE'),
         ([5,18,29,42],'0.1_PFF','ONE'),
         ([7,16,31,40],'1_PFF','ONE')]

condition=[[df2.columns[-1], 'Normalized agg. area', 'aggregate area/ \n cell area'],
           ['cell_area_norm','Cell density ' ,'cell coverage\n($um^2$)'],
           ['total_agg_area','Aggregate area','aggregates/field \n($um^2$)']]

for sample in samples:
   for cond in condition:
      save_name=' | '.join([cond[1],sample[1],sample[2]])
      ylab=cond[2]
      graph(sample[0], cond[0], ylab, save_name)

#%% Graph generator - fixed oligo
def graph(samples, condition,ylab,save_name):
   legends=[]
   y_max=0
   for v in samples:
      well=df2[df2['well']==str(v)]
      start=list(well[well['timepoint']==0]['cell_area'])
      well['cell_area_norm']=(well['cell_area']/start)*100
      if y_max< np.amax(well[condition]):
         y_max=np.amax(well[condition])
      r=sns.regplot(x="timepoint", y=condition, data=well,
                    scatter_kws={"s": 10},
                    order=3, ci=None)
      legends.append(well.iloc[0]['oligo']+r" $\frac{ug}{ml}$ "+well.iloc[0]['oligo_type']+" / "+well.iloc[0]['PFF']+r" $\frac{ug}{ml}$ PFF")
   r.spines['right'].set_visible(False)
   r.spines['top'].set_visible(False)
   r.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5),prop={'size': 8})
   
   plt.xlim((0,49))
   plt.ylim((0, y_max*1.1))
   plt.ylabel(ylab)
   plt.xlabel('duration \n ($hours$)')
   # plt.title(title, size=20)
   plt.tight_layout()
   plt.savefig(save_name+".png", dpi=300, figsize=(20,10))
   plt.show()
   plt.clf()
   
samples=[([49,51,53,55],'0.01_HNE','HNE'),
         ([68,66,64,62],'0.1_HNE','HNE'),
         ([71,73,75,77],'1_HNE','HNE'),
         ([90,88,86,84],'10_HNE','HNE'),
         ([1,3,5,7],'0.01_ONE','ONE'),
         ([22,20,18,16],'0.1_ONE','ONE'),
         ([25,27,29,31],'1_ONE','ONE'),
         ([46,44,42,40],'10_ONE','ONE')]

condition=[[df2.columns[-1], 'Normalized agg. area', 'aggregate area/ \n cell area'],
           ['cell_area_norm','Cell density ' ,'cell coverage\n($um^2$)'],
           ['total_agg_area','Aggregate area','aggregates/field \n($um^2$)']]
#%%

img=nd2.ND2Reader('/media/data/Jan/20191205 - ONE-HNE/Oligo002.nd2')
img.bundle_axes='yx'
img.default_coords['t'] = 96
img.iter_axes='v'
img

def graph2(samples, condition,ylab,ax):
   legends=[]
   y_max=0
   for v in samples:
      well=df2[df2['well']==str(v)]
      start=list(well[well['timepoint']==0]['cell_area'])
      well['cell_area_norm']=(well['cell_area']/start)*100
      if y_max< np.amax(well[condition]):
         y_max=np.amax(well[condition])
      ax=sns.regplot(x="timepoint", y=condition, data=well,
                    scatter_kws={"s": 10},
                    order=3, ci=None)
      legends.append(well.iloc[0]['oligo']+r" $\frac{ug}{ml}$ "+well.iloc[0]['oligo_type']+" / "+well.iloc[0]['PFF']+r" $\frac{ug}{ml}$ PFF")
   ax.spines['right'].set_visible(False)
   ax.spines['top'].set_visible(False)
   ax.legend(legends, loc='center left', bbox_to_anchor=(1.05,0.5),prop={'size': 8})
   
   plt.xlim((0,49))
   plt.ylim((0, y_max*1.1))
   plt.ylabel(ylab)
   plt.xlabel('duration \n ($hours$)')
   # plt.title(title, size=20)
   plt.tight_layout()
   # plt.savefig(save_name+".png", dpi=300, figsize=(20,10))
   # plt.show()
   # plt.clf()



fig1, axes=plt.subplots(2,4, figsize=(20,10),constrained_layout=True)
axes[0,0].imshow(img[7], cmap='gray')
axes[0,1].imshow(img[16], cmap='gray')
axes[0,2].imshow(img[31], cmap='gray')
axes[0,3].imshow(img[40], cmap='gray')
axes[1,0].imshow(img[54], cmap='gray')
axes[1,1].imshow(img[62], cmap='gray')
axes[1,2].imshow(img[77], cmap='gray')   
axes[1,3].imshow(img[84], cmap='gray')

for ax in axes.ravel():
   ax.set_axis_off()

plt.tight_layout()
plt.savefig('pictures.png', dpi=300)