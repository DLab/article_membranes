import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('lectura de datos fi lista_sim Matrix')

fi = pd.read_csv('./FI.csv') 
lista = pd.read_csv('./lista_peli.csv') 

#unificar: fi sim0 a sim n concadenados
fi_vector=[]
contador=0
for i in list(fi)[1:]:
    inicio=int((50000-(lista['1'][contador]))/10)
    fi_vector.extend(np.array(fi[str(i)][inicio:]))
    contador=contador+1

fi_vector=pd.DataFrame(fi_vector)
fi_vector.to_csv('FI_vector.csv')
