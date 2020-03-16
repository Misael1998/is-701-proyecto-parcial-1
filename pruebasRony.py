import pandas as pd
import numpy as np

datos = pd.read_csv("datosR.csv")

datos2 = pd.read_csv("test_data_1.csv")

def get_first_n_rows(dataset, n):
  """Retorna un DataFrame que contiene las primeras <n> filas de <dataset>"""
  newData = dataset.head(n)
  return newData

def get_last_n_rows(dataset, n):
  """Retorna un DataFrame que contiene las últimas <n> filas de <dataset>"""
  newData = dataset.tail(n)
  return newData

def remove_cols_with_nulls(dataset):
  """Retorna <dataset> con todas las columnas que tienen datos de tipo null removidas."""
  colNUll = dataset.isnull().any()
  numCol = dataset.columns[colNUll]
  index = numCol.values
  newData = dataset.drop(index, axis=1)
  return newData

def filter_by_col(dataset, column_name, value):
  """Filtra <dataset> retornando un DataFrame que sólo contiene las filas donde el valor de la 
  columna <column_name> es igual a <value>"""
  filterData = dataset[dataset[column_name] == value]
  return filterData

#print(datos)  

print("\n")  

print("Resultado de get_first_n_rows: \n",get_first_n_rows(datos, 2))
print("*******************************************************************************")
print("Resultado de get_last_n_rows: \n",get_last_n_rows(datos, 2))
print("*******************************************************************************")
print("Resultado de remove_cols_with_nulls: \n",remove_cols_with_nulls(datos))
print("*******************************************************************************")
print("Resultado de filter_by_col: \n",filter_by_col(datos, 'apellido', 'Rodriguez'))