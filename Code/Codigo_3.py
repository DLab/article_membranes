import os
import pandas as pd


path_in='../proteinas_cortadas_cambio_nombre/'

path_out='../sim_unidas/'

try:
    os.mkdir(path_out)
except OSError:
    print (" ")
else:
    print (" ")


#leer documento csv lista
lista=pd.read_csv('lista_peli.csv') 

os.chdir('../proteinas_cortadas_cambio_nombre/')
print(os.getcwd())


lss = os.listdir('./')
print(lss)

arg1=''
arg2='md_prot_charmm_50ns_310K_E=0,2_minim_simunidas.trr'

for i in lista['0']:
    arg1=arg1+' '+i
    
os.system('gmx trjcat -f '+arg1+' -o '+path_out+arg2)


