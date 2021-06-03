import os
import numpy as np

path_codigo4='codigo_4'
path_TG='TODOS_GRO'

try:
    os.mkdir(path_codigo4)
 
except OSError:
    print (" ")
else:
    print (" ")


try:

    os.mkdir(path_TG)
except OSError:
    print (" ")
else:
    print (" ")

nom='md_prot_charmm_50ns_310K_E=0,2_minim_simunidas'
path_out='./'+path_TG+'/'
arg1='../../sim_unidas/md_prot_charmm_50ns_310K_E=0,2_minim_simunidas.trr'
arg2='../../proteina_all/prot.tpr'
nn=0

grupo=0
comando=''
n=0
nombre=0


#crear 60.sh con head
grupo=0
for i in range(60):
	f= open(path_codigo4+'/comandos_'+str(grupo)+'.sh',"w+")
	f.write('#!/bin/bash\n')
	f.write('#SBATCH --job-name=SC_50ns_75chol_E=0,1\n')
	f.write('#SBATCH --output=SC_50ns_75chol.txt\n\r')
	f.write('#SBATCH --ntasks=1\n')
	f.write('#SBATCH --mail-user=arruiz@ug.uchile.cl\n')
	f.write('#SBATCH --mail-type=END\n')
	f.write('#SBATCH --partition=pollux\n')
	f.write('\n')
	f.close()
	grupo=grupo+1
	#print(grupo)
#48623
nodo=0
for i in range(48623):

	with open(path_codigo4+'/comandos_'+str(nodo)+'.sh', "a") as file_object:
		comando='gmx trjconv -f '+arg1+' -s '+arg2+' -b '+str(nombre)+' -e '+str(nombre)+' -o '+str(path_out)+str(nom)+'_'+str(nombre)+'.gro < ../prot_1.txt'
		file_object.write('\n'+comando)
		file_object.close()
	nombre=nombre+10

	nodo=nodo+1
	if(nodo==60):
		nodo=0
	

	


		
f= open('Codigo_4.sh',"w+")

lista = os.listdir('./codigo_4')
lista=sorted(lista,key=len)

for i in lista:
    f.write('sbatch '+str(i)+'\n')
f.close()
