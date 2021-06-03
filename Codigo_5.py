import os


path='Codigo_5'
path_TT='./'+path+'/TODOS_TPR'
try:

    os.mkdir(path)
    os.mkdir(path_TT)

except OSError:
    print ("existe")
else:
    print ("crear carpeta Codigo_5")

try:


    os.mkdir(path_TT)

except OSError:
    print ("existe")
else:
    print ("crear carpeta Codigo_5")


lista = os.listdir('./codigo_4/TODOS_GRO')
lista=sorted(lista,key=len)
#print(lista)

grupo=0
comando=''
n=0
for i in lista:
	if(i.split('.')[1]=='gro'):
		if(n==0):
			f= open(path+'/comandos_'+str(grupo)+'.sh',"w+")
			f.write('#!/bin/bash\n')
			f.write('#SBATCH --job-name=SC_50ns_75chol_E=0,1\n')
			f.write('#SBATCH --output=SC_50ns_75chol.txt\n\r')
			f.write('#SBATCH --ntasks=1\n')
			f.write('#SBATCH --mail-user=arruiz@ug.uchile.cl\n')
			f.write('#SBATCH --mail-type=END\n')
			f.write('#SBATCH --partition=pollux\n')
			f.write('\n')
			comando='gmx grompp -f minim.mdp -c ../codigo_4/TODOS_GRO/'+i+' -p topol_prot.top -o ./TODOS_TPR/'+i[:-3]+'tpr -maxwarn 1'
			f.write(comando+'\n')
		if(n>=1):
			comando='gmx grompp -f minim.mdp -c ../codigo_4/TODOS_GRO/'+i+' -p topol_prot.top -o ./TODOS_TPR/'+i[:-3]+'tpr -maxwarn 1'
			f.write(comando+'\n')
		n=n+1
		if(n==(811)):
			f.close()
			#os.system(comando)
			comando=''
			n=0
			grupo=grupo+1


		
f= open('Codigo_5.sh',"w+")

lista = os.listdir('./Codigo_5')
lista=sorted(lista,key=len)

for i in lista:
    f.write('sbatch '+str(i)+'\n')
f.close()
