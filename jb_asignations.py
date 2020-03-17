import pandas as pd


data = pd.read_csv("test_data_1.csv")
dt=pd.DataFrame(data)

'''

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
    pass

'''
func_shape = get_shape(data)
print ('Resultado de la funcion get_shape():\n', func_shape)

print('\n')
list_name_col= ['Column_1','Column_2','Column_3','Column_4','Column_5','Column_6','Column_7','Column_8','Column_9','Column_10','Column_11','Column_12']
chan_col_names = change_column_names(data, list_name_col)
print ('Resultado de la funcion change_column_names():\n', chan_col_names)

print('\n')
slice_row = get_slice(data, 1,4)
print(slice_row)

'''

