# -*- coding: utf-8 -*-
"""


@author: Elsy

Elsy Yuliana Silgado Rivera
ID: 502194
elsy.silgado@upb.edu.co

"""
#Importamos la librerias
import pandas as pd
import random
import numpy as np

#Definimos la varibales, y con el metod pandas leemos el archivo csv
data = pd.read_csv('netflix_titles.csv')

# Imprima por consola las primeras y últimas 5 filas del arreglo.
print(data.head(5))

print(data.tail(5))

# Imprima cada uno de los tipos de dato asociado a las etiquetas.
print(data.dtypes)

# Guarde un archivo .xlsx, en el cual el nombre del archivo sea “Netflix_list” y el nombre de la hoja sea “títulos”
data.to_excel("Netflix_list.xlsx", sheet_name="títulos", index=False)

#Cree una nueva data frame en el cual segmente únicamente: el tipo, la duración, la descripción y el país
ndata = data.loc[:,['type','duration','description','country']]

# Campo con duracion en numerico
data["duracion"] = pd.to_numeric(data['duration'].replace('([^0-9]*)','', regex=True), errors='coerce')

# Haga un filtro para las películas que tienen una duración superior a 100 min
movies_100 = data[data['type'].str.contains('Movie', na=False)]
movies_100_min = movies_100[movies_100['duracion']>100]

#Haga un filtro para los “TV Shows” que tienen más de 3 temporadas.
tv = data[data['type'].str.contains('TV Show', na=False)]
tv_3= tv[tv['duracion']>3]

#Haga un filtro en el cual solo tenga en cuenta 2 categorías/etiquetas (libre elección)
categorias = data.loc[data['listed_in'].isin(['Documentaries','International TV Shows, TV Dramas, TV Mysteries'])]

# Recuerde usar casos con indexación numérica y con texto (loc / iloc).
# Modifique los valores del ID de las 5 primeras y las 5 últimas “shows” y de cualquier otra etiqueta de su elección (solo un valor).
data.iloc[:4,0]='s1'
tv.loc[1431:,'listed_in']='Comedies, Horror Movies'

#Añada una nueva columna “Visto”, en la cual debe colocar 1/0 (aleatorio) si vio o no el show (simulación).

data["Visto"] = np.random.randint(0, 3, data.shape[0])


