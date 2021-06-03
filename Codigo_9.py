import MDAnalysis as mda
from MDAnalysis.tests.datafiles import PSF, DCD
from MDAnalysis.analysis import contacts

import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from MDAnalysis.tests.datafiles import TRR,TPR
import MDAnalysis.analysis.rms

n=8#radio

path='./'
pathtrr='../proteina_all/'
data = pd.read_csv(path+"lista_rms_corte.csv") 

fi1=pd.DataFrame({})
contador=0
for i in data['0']:
    if(i.find('_')==-1):
        punto='md_prot_charmm_50ns_310K_E=0,2_minim.trr'
    elif i.find('_')!=-1:
        punto = 'md_prot_charmm_50ns_310K_E=0,2_minim_'+str(i.split('_')[1])+'.trr'
    print(punto)
    
    trr = pathtrr+punto
    tpr = pathtrr+'prot.tpr'
    print(tpr)
    u = MDAnalysis.Universe(tpr, trr)
    q1q2 = contacts.q1q2(u, 'name CA', radius=n).run()
    q1q2_df = pd.DataFrame(q1q2.timeseries,columns=['Frame','Q1','Q2'])
    
    fi1.insert(contador,str(punto[38:-4]),q1q2_df['Q1'])
    contador=contador+1
fi1.to_csv('FI.csv')
