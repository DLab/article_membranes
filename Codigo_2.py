import os
import pandas as pd


path_in='../proteina_all/'
path_out='../proteinas_cortadas_tx/'
path_out_n='../proteinas_cortadas_cambio_nombre/'

path_codigo2='codigo_2'
try:

    os.mkdir(path_out)
    os.mkdir(path_out_n)

    os.mkdir(path_codigo2)

except OSError:
    print (" ")
else:
    print (" ")



#leer documento csv lista
lista=pd.read_csv('lista_rms_corte.csv') 
lista_peli=[]
ta=0

for i in lista['Unnamed: 0']:

    arch='md_prot_charmm_50ns_310K_E=0,2_minim'+lista['0'][i][4:]+'.trr'
    arg1=path_in+arch
    arg2=path_in+'prot.tpr'
    arg3=int(lista['1'][i])*10
    arg4=path_out+arch[:-4]+'_'+str(arg3)+'-50000ps.trr'
    diferencia=50000-arg3

    f= open(path_codigo2+'/'+'comandos'+str(lista['0'][i][4:])+'.sh',"w+")
    f.write('#!/bin/bash\n')
    f.write('#SBATCH --job-name=SC_50ns_75chol_E=0,1\n')
    f.write('#SBATCH --output=SC_50ns_75chol.txt\n\r')
    f.write('#SBATCH --ntasks=1\n')
    f.write('#SBATCH --mail-user=arruiz@ug.uchile.cl\n')
    f.write('#SBATCH --mail-type=END\n')
    f.write('#SBATCH --partition=pollux\n')
    f.write('\n')
    
    comando='gmx trjconv -f '+arg1+' -s '+arg2+' -b '+str(arg3)+' -e 50000 -o '+arg4+'< prot_1.txt'
    f.write(comando+'\n')

    comando='gmx trjconv -t0 '+str(ta)+' -f '+arg4+' -o '+path_out_n+arch[:-4]+'_'+str(ta)+'-'+str(ta+diferencia)+'ps.trr'
    f.write(comando+'\n')
    f.close()
    lista_peli.append([arch[:-4]+'_'+str(ta)+'-'+str(ta+diferencia)+'ps.trr',diferencia,ta])
    ta=ta+diferencia+10

lista_peli=pd.DataFrame(lista_peli)
lista_peli.to_csv('lista_peli.csv')


f= open('Codigo_2.sh',"w+")

lista = os.listdir('./codigo_2')
lista=sorted(lista,key=len)


for i in lista:
    f.write('sbatch ./'+path_codigo2+'/'+str(i)+'\n')
f.close()