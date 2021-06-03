import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import collections
import math 
import numpy as np
import statsmodels.api as sm

lowess = sm.nonparametric.lowess

path_plot = "./rmps_plot"

try:
    os.mkdir(path_plot)
except OSError:
    print ("Creation of the directory %s failed" % path_plot)
else:
    print ("Successfully created the directory %s " % path_plot)

path_Dataframe = "./rmps_dataframe"

try:
    os.mkdir(path_Dataframe)
except OSError:
    print ("Creation of the directory %s failed" % path_Dataframe)
else:
    print ("Successfully created the directory %s " % path_Dataframe)

RMSD_sim = os.listdir('../rms_prot_all/')
RMSD_sim=sorted(RMSD_sim,key=len)

sim_RMSD_df=pd.DataFrame({})
n=0
for i in RMSD_sim:
    if(i.split('.')[-1]=='xvg'):
        
        nombre=i.split('minim')[1].split('.')[0]
        print(nombre)

        with open('../rms_prot_all/'+i) as f:
            data = f.read()
            data = data.split('\n')
        sim_temp=[]
        
        for i in range(len(data[18:])-1):
            valor=float(data[18:][i][15:])
            sim_temp.append(valor)
        
        sim_RMSD_df.insert(n,'Rmsd'+str(nombre),sim_temp)  
        n=n+1


print('Rmsd')
sim_min=sim_RMSD_df[min(sim_RMSD_df)].min()
sim_max=sim_RMSD_df[max(sim_RMSD_df)].max()
print('max:',sim_max)
print('min:',sim_min)

sim_rmsd_nom=((sim_RMSD_df[:]-sim_min)/(sim_max-sim_min))

#plt.figure(figsize=(20,10))
#for i in range(len(list(sim_RMSD_df))-1):
#    plt.plot(sim_RMSD_df[list(sim_RMSD_df)[i+1]][0:5000])
#plt.show

lista_ok=[]



for l in list(sim_RMSD_df):

    DFtemporal=[]
    print(l)
    #promedio n puntos
    #lowess
    x = np.array(sim_RMSD_df[l])
    y = np.sin(x)
    z = lowess(y, x,frac= 1./2, it=0)
    w = lowess(y, x, frac=1./2)
    W=pd.DataFrame(w)
    #plt.figure(figsize=(40,20))
    #plt.grid()
    #plt.plot(W[0],'-')
    #plt.plot(x,'--')

    #######

    dato=[]
    a=0
    d=0
    promc=30 #promedio de n

    for i in W[0]:
        d=d+i
        if a==promc:
            dato.append(d/a)
            #print(d/a)
            a=0
            d=0
        a=a+1

    dt = np.linspace(0, 5000, int(5000/promc)) 
    dt_col = np.linspace(0, 5000, int(5000/promc)) 


    #pendiente
    col_df=pd.DataFrame({})
    col=[]
    col.append(0)
    for i in range(len(dato)-1):
            y1=dato[i]
            y2=dato[i+1]
            m=(y2-y1)/2
            col.append(m)
    col_df.insert(0,'0',col)
    

    #norm
    sim_min=col_df['0'].min()
    sim_max=col_df['0'].max()
    col_df_nom=((col_df[:]-sim_min)/(sim_max-sim_min))
    

    prom=[]
    c=0
    for i in range(len(col_df_nom['0'])):
        t=col_df_nom['0'][i:].sum()/col_df_nom['0'].sum()
        prom.append(t)
        if(c==0):
            if(t<=0.1):
                c=1
                if(5000-(i*promc)>1000):
                    #print(5000-(i*30),l)
                    lista_ok.append([str(l),int(i*promc)])
                    plt.plot([int(i*promc),int(i*promc)],[0,1],"-rx", markersize=5)
    
    #plt
    plt.grid()
    plt.plot(sim_RMSD_df[l],"-ro", markersize=1)
    plt.plot(dt,dato,"-go", markersize=5)
    plt.plot(dt,prom,"-ro", markersize=5)
    plt.plot(dt,col_df_nom,"-bo", markersize=5 ,label=str(l))
    plt.legend()
    plt.show
    plt.savefig(path_plot+'/'+str(l)+'_cut.png')
    DFtemporal.append([str(l),sim_RMSD_df[l],dato,prom,col_df_nom])
    DFtemporal=pd.DataFrame(DFtemporal)
    DFtemporal.to_csv(path_Dataframe+'/dataframe_sim_'+str(l)+'.csv')


lista_ok=pd.DataFrame(lista_ok)
lista_ok.to_csv('lista_rms_corte.csv') 