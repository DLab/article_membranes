#!/usr/bin/python3
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import collections
from tqdm import tqdm

dt=100
#crear matris 1d
path='/home/Cx/kronos/alvaro/codes/codigos/Codigo_6/TODOS_XVG'

XVG_path = os.listdir(path)
XVG_list=sorted(XVG_path,key=len)


RMSD_df=pd.DataFrame({})
RMSD_df_name=pd.DataFrame({})

n=0
for i in tqdm(XVG_list):
    if(i.split('.')[-1]=='xvg'):
        
        col_name=i.split('_')[8][:-4]
        
        with open(path+'/'+i) as f:
            data = f.read()
            data = data.split('\n')
            
        i_temp=[]
        
        for i in data[18:]:
            #print(i.split('   ')[1])
            i_temp.append(i.split('   ')) 
        df=pd.DataFrame(i_temp)
        RMSD_df.insert(n,str(col_name),df[1][:])  
        n=n+1   

RMSD_df.to_csv (r'MATRIX_'+str(dt)+'.csv', index = True, header=True)





