import pandas as pd

def get_shape(dataset):
    """Retorna una tupla con las dimensiones del DataFrame <dataset>"""
    dt=pd.DataFrame(dataset)
    shape = dt.shape
    return shape

def change_column_names(dataset, new_names):
    """Retorna un DataFrame cuyas columnas han sido renombradas de acuerdo a los nombres proporcionados en <new_names> que es una lista de strings."""
    dt=pd.DataFrame(dataset)
    if len(new_names) == len(dt.columns) :
        dt.columns = new_names
        return dt
    else:
        return 'Para cambiar los nombres de las columnas debe mandar una lista de nombres con la misma cantidad de columnas'

def get_slice(dataset, start, end):
    """Retorna un DataFrame formado por un grupo de filas de <dataset>, desde la fila en la posición
    <start> hasta la fila en la posición <end> - 1"""
    dt=pd.DataFrame(dataset)
    rows = dt.iloc[start:end]
    return rows

def fill_numeric_nulls(dataset): 
    """Retorna <dataset> con sus valores numéricos faltantes sustituídos por el valor de la media de la columna a la que pertenecen y los no numéricos se dejan tal como están."""
    dt=pd.DataFrame(dataset)
    col_num=[]
    #numero de filas
    len(dt.index)
    #print(len(dt.columns))
    for i in range(len(dt.columns)):
        #Nombre de columna
        name_column=dt.columns[i]
        #iterando cada una de las columnas para ver cuales son columnas numericas
        p= True if (dt[name_column].dtypes == 'int64') or (dt[name_column].dtypes == 'float64') else False
        #Si la name_column es numerica, el nombre de la name_column se guardara en una lista col_num
        if p == True:
            col_num.append(name_column)
    #recorrer todo el arreglo columnas numericas
    for e in col_num:
        average = 0
        #Convertir todo a numero, pero si no es numero lo convierte en NaN
        pd.to_numeric(dt[e], errors='coerce')
        average = (dt[e].sum())/(len(dt) - (dt[e].isnull().sum()))
        #reemplazar NaN
        dt[e].fillna(average, inplace=True)
    return dt

data = pd.read_csv("test_data_1.csv")
dt=pd.DataFrame(data)

func_shape = get_shape(data)
print ('Resultado de la funcion get_shape():\n', func_shape)

list_name_col= ['Column_1','Column_2','Column_3','Column_4','Column_5','Column_6','Column_7','Column_8','Column_9','Column_10','Column_11','Column_12']
chan_col_names = change_column_names(data, list_name_col)
print ('\nResultado de la funcion change_column_names():\n', chan_col_names)

slice_row = get_slice(data, 1,4)
print('\nEl resultado de la funcion get_slice():\n',slice_row)

fill_num = fill_numeric_nulls(data)
print('\nEl resultado de la funcion fill_numeric_nulls():\n',fill_num)


##############################       TEST      #################################
'''
#Encontrar cuantos NaN hay en la columna
#nan= dt['Rank'].isnull().sum()
#print(nan)
#Imprimir los valores de una columna
#print(dt['Rank'])

#Sumar los valores de la columna, esta funcion obvia los NaN
#print(dt['Rank'].sum())

#Imprimir el nombre de una columna
#print(dt.columns[0])

#numero de valores
#len(dt)

#Encontrar la media de la columna. Al total de filas se le resta la cantidad de NaN
#average = (dt['Rank'].sum())/(len(dt) - (dt['Rank'].isnull().sum()))
#print(average)

#numero de filas
#len(dt.index)


#############################FUNCION fill_numeric_nulls ###########################
col_num=[]
#numero de filas
len(dt.index)
#print(len(dt.columns))
for i in range(len(dt.columns)):
    #Nombre de columna
    name_column=dt.columns[i]
    #iterando cada una de las columnas para ver cuales son columnas numericas
    p= True if (dt[name_column].dtypes == 'int64') or (dt[name_column].dtypes == 'float64') else False
    #Si la name_column es numerica, el nombre de la name_column se guardara en una lista col_num
    if p == True:
        col_num.append(name_column)
#print(col_num)

#print (dt[col_num[0]].mean())

#recorrer todo el arreglo columnas numericas
for e in col_num:
    average = 0
    #Convertir todo a numero, pero si no es numero lo convierte en NaN
    pd.to_numeric(dt[e], errors='coerce')
    average = (dt[e].sum())/(len(dt) - (dt[e].isnull().sum()))
    #reemplazar NaN
    dt[e].fillna(average, inplace=True)
    print(dt[e])

###################################################################################


#Convertir todo a numero, pero si no es numero lo convierte en NaN
pd.to_numeric(dt[col_num[0]], errors='coerce')
#Encontrar la media de la columna. Al total de filas se le resta la cantidad de NaN
average = (dt['Rank'].sum())/(len(dt) - (dt['Rank'].isnull().sum()))
#reemplazar NaN
dt[col_num[0]].fillna(0, inplace=True)
print (dt[col_num[0]])



columna=dt.columns[0]
p= True if (dt[columna].dtypes == 'int64') or (dt[columna].dtypes == 'float64') else False

if p == True:
    print(dt[columna].dtypes)

#print(p)

#print(dt.dtypes)


shape = dt.shape
print(dt)
print(shape)

list_columns= ['Column_1','Column_2','Column_3','Column_4','Column_5','Column_6','Column_7','Column_8','Column_9','Column_10','Column_11','Column_12',]
dt.columns = list_columns
print(dt)
print(len(list_columns))

start=0
end = 3
rows= dt.iloc[start:end]
print(rows)
'''