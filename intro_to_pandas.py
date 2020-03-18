import pandas as pd

# Evaluación
# get_dataset_from_csv(filename, index_col_num):  5 misael
# get_custom_dataset(data_dict, index_name):      5 misael
# get_first_n_rows(dataset, n):                   5 rony
# get_last_n_rows(dataset, n):                    5 rony
# get_shape(dataset):                             5 jheral
# change_column_names(dataset, new_names):        5 jheral
# count_nulls_per_column(dataset):                8 misael 
# remove_cols_with_nulls(dataset):                8 rony
# get_slice(dataset, start, end):                 8 jheral
# filter_by_col(dataset, column_name, value):     8 rony
# fill_numeric_nulls(dataset):                    15 jheral
# get_most_correlated_cols(dataset, umbral):      23 misael
#                                         TOTAL   100

def get_dataset_from_csv(filename, index_col_num):
  """Retorna un DataFrame leyendolo desde el archivo <filename>, define la columna en la posicion <index_col_num> como índice de éste."""
  path = filename
  df = pd.read_csv(path, index_col = index_col_num)

  return df

def get_custom_dataset(data_dict, index_name):
  """Retorna un DataFrame a partir del diccionario <data_dict>, define la columna <index_name> como
  índice del dataset"""

  data = data_dict
  df = pd.DataFrame(data)
  df.set_index(index_name)

  return df

def get_first_n_rows(dataset, n):
  """Retorna un DataFrame que contiene las primeras <n> filas de <dataset>"""
  newData = dataset.head(n)
  return newData
  #pass

def get_last_n_rows(dataset, n):
  """Retorna un DataFrame que contiene las últimas <n> filas de <dataset>"""
  newData = dataset.tail(n)
  return newData
  #pass

def get_shape(dataset):
  """Retorna una tupla con las dimensiones del DataFrame <dataset>"""
  dt=pd.DataFrame(dataset)
  shape = dt.shape
  return shape

def change_column_names(dataset, new_names):
  """Retorna un DataFrame cuyas columnas han sido renombradas de acuerdo a los nombres proporcionados en <new_names> que es una lista de strings."""
  dt=pd.DataFrame(dataset)
  dt.columns = new_names
  return dt

def count_nulls_per_column(dataset):
  """Retorna una Serie (columna) que contiene como índice los nombres de las columnas del 
    <dataset> y en sus datos el total de elementos de tipo null o na que se encuentran en cada una.
  """
  pass

def remove_cols_with_nulls(dataset):
  """Retorna <dataset> con todas las columnas que tienen datos de tipo null removidas."""
  colNUll = dataset.isnull().any()
  numCol = dataset.columns[colNUll]
  index = numCol.values
  newData = dataset.drop(index, axis=1)
  return newData
  #pass

def get_slice(dataset, start, end):
  """Retorna un DataFrame formado por un grupo de filas de <dataset>, desde la fila en la posición
  <start> hasta la fila en la posición <end> - 1"""
  dt=pd.DataFrame(dataset)
  rows = dt.iloc[start:end]
  return rows

def filter_by_col(dataset, column_name, value):
  """Filtra <dataset> retornando un DataFrame que sólo contiene las filas donde el valor de la 
  columna <column_name> es igual a <value>"""
  filterData = dataset[dataset[column_name] == value]
  return filterData
  #pass

def fill_numeric_nulls(dataset): 
  """Retorna <dataset> con sus los valores numéricos faltantes se sustituídos por el valor de la media de la columna a la que pertenecen y los no numéricos se dejan tal como están."""
  dt=pd.DataFrame(dataset)
  col_num=[]
  len(dt.index)
  for i in range(len(dt.columns)):
    name_column=dt.columns[i]
    p= True if (dt[name_column].dtypes == 'int64') or (dt[name_column].dtypes == 'float64') else False
    if p == True:
      col_num.append(name_column)
  for e in col_num:
    average = 0
    if (dt[e].isnull().sum()>0):
      pd.to_numeric(dt[e], errors='coerce')
      average = (dt[e].sum())/(len(dt) - (dt[e].isnull().sum()))
      dt[e].fillna(average, inplace=True)
  return dt

def get_most_correlated_cols(dataset, umbral): 
  """Retorna un conjunto de frozensets con los pares de columnas cuyas correlaciones positivas o negativas segan mayores o iguales a <umbral>."""
  pass
  