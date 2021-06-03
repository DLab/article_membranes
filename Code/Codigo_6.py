import os

path='Codigo_6'
print('Codigo 6')

path_tpr='./Codigo_5/TODOS_TPR/'
path_xvg='./Codigo_6/TODOS_XVG/'
try:
    os.mkdir(path)
except OSError:
    print ("existe")
else:
    print ("crear carpeta Codigo_6")

try:
    os.mkdir(path_xvg)
except OSError:
    print ("existe")
else:
    print ("crear carpeta Codigo_6")


lista = os.listdir(path_tpr)
lista=sorted(lista,key=len)

print(path_tpr,len(lista))




grupo=0
comando=''
n=0

for i in lista:
	if(i.split('.')[1]=='tpr'):
		if(n==0):
			f= open('./Codigo_6/comandos_'+str(grupo)+'.sh',"w+")
			f.write('#!/bin/bash\n')
			f.write('#SBATCH --job-name=SC_50ns_75chol_E=0,1\n')
			f.write('#SBATCH --output=SC_50ns_75chol.txt\n\r')
			f.write('#SBATCH --ntasks=1\n')
			f.write('#SBATCH --mail-user=arruiz@ug.uchile.cl\n')
			f.write('#SBATCH --mail-type=END\n')
			f.write('#SBATCH --partition=pollux\n')
			f.write('\n')
			comando='gmx rms -f ../../sim_unidas/md_prot_charmm_50ns_310K_E=0,2_minim_simunidas.trr -s ../Codigo_5/TODOS_TPR/'+i+' -o ./TODOS_XVG/'+i[:-3]+'xvg < calpha.txt'
			f.write(comando+'\n')
		if(n>=1):
			comando='gmx rms -f ../../sim_unidas/md_prot_charmm_50ns_310K_E=0,2_minim_simunidas.trr -s ../Codigo_5/TODOS_TPR/'+i+' -o ./TODOS_XVG/'+i[:-3]+'xvg < calpha.txt'
			f.write(comando+'\n')
		n=n+1
		if(n==811):
			f.close()
			#os.system(comando)
			comando=''
			n=0
			grupo=grupo+1

f= open('./Codigo_6/Codigo_6.sh',"w+")

lista = os.listdir('./Codigo_6')
lista=sorted(lista,key=len)

for i in lista:
    f.write('sbatch '+str(i)+'\n')
f.close()


