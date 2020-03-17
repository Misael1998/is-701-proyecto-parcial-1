# Evaluation Resume
# get_dataset_from_csv(filename, index_col_num):  5
# get_custom_dataset(data_dict, index_name):      5
# get_first_n_rows(dataset, n):                   5
# get_last_n_rows(dataset, n):                    5
# get_shape(dataset):                             5
# change_column_names(dataset, new_names):        5
# count_nulls_per_column(dataset):                8
# remove_cols_with_nulls(dataset):                8
# get_slice(dataset, start, end):                 8
# filter_by_col(dataset, column_name, value):     8
# fill_numeric_nulls(dataset):                    15
# get_most_correlated_cols(dataset, umbral):      23
#                                         TOTAL   100
import numpy as np
grade = 100

def end_and_print_grade():
  print('=' * 79)
  if grade == 100:
    print('¡Felicidades no se detectó ningún error!')
  print(('Su nota asignada es: NOTA<<{0}>>').format(grade if grade >= 0 else 0))
  exit()

def print_function_error(function_name, error):
  print('Error en la función ' + function_name)
  print(('El error recibido fue:\n{0}\n\n').format(error))


def equal_dataframes(ds1, ds2):
  # return (ds1.dropna(axis=1) == ds2.dropna(axis=1)).all().all()
  return ds1.equals(ds2)

try:
  from intro_to_pandas import *
except Exception as e:
  print('Error al importar del módulo intro_to_pandas')
  print(('El error recibido fue:\n{0}').format(e))
  grade = 0
  end_and_print_grade()

try:
  ds = get_dataset_from_csv("test_dataset.csv", 0)
  if (ds.shape != (1000,11)):
    raise Exception('Las dimensiones del DataFrame leído son incorrectas (-100%)')
    if (ds.index.name != "Rank"):
      raise Exception('El DataFrame creado no tiene el indice solicitado (-100%)')
except Exception as e:
  print_function_error('get_dataset_from_csv', e)
  grade = 0
  end_and_print_grade()

try:
  res = get_custom_dataset({
          'manzanas': [3, 2, 0, 1], 
          'naranjas': [0, 3, 7, 2]
          }, "manzanas")
  if (res.shape != (4,1)):
    raise Exception('Las dimensiones del DataFrame creado son incorrectas (-5%)')
    if (res.index.name != "manzanas"):
      raise Exception('El DataFrame creado no tiene el indice solicitado (-5%)')
except Exception as e:
  print_function_error('get_custom_dataset', e)
  grade -= 5


# ds debe existir si se llega a este punto, 
# la función get_dataset_from_csv también debe de funcionar bien
try:
  ds = get_dataset_from_csv("test_dataset.csv", 0)
  res = get_first_n_rows(ds, 5)
  test = get_dataset_from_csv("test_data_1.csv", 0)
  if ( not (res == test).all().all() ):
    raise Exception('No se devolvio las primeras n filas solicitadas (-5%)')
except Exception as e:
  print_function_error('get_first_n_rows', e)
  grade -= 5

try:
  ds = get_dataset_from_csv("test_dataset.csv", 0)
  res = get_last_n_rows(ds, 5)
  test = get_dataset_from_csv("test_data_2.csv", 0)
  if not equal_dataframes(res, test):
    raise Exception('No se devolvio las ultimas n filas solicitadas (-5%)')
except Exception as e:
  print_function_error('get_last_n_rows', e)
  grade -= 5

try:
  ds = get_dataset_from_csv("test_dataset.csv", 0)
  res = get_shape(ds)
  if (res != (1000,11)):
    raise Exception('Las dimensiones del DataFrame obtenidas son incorrectas (-5%)')
except Exception as e:
  print_function_error('get_shape', e)
  grade -= 5

try:
  ds = get_dataset_from_csv("test_dataset.csv", 0)
  new_names = [ c.lower() for c in ds ]
  new_ds = change_column_names(ds, new_names)
  if (new_ds.columns.to_list() != new_names):
    raise Exception('Las columnas del nuevo DataFrame no tienen los nombres solicitados (-5%)')
except Exception as e:
  print_function_error('change_column_names', e)
  grade -= 5

try:
  ds = get_dataset_from_csv("test_dataset.csv", 0)
  res = count_nulls_per_column(ds)
  if not isinstance(res, pd.core.series.Series):
    raise Exception('No se retorna un objeto de tipo pandas.core.series.Series (-8%)')
  else:  
    if not (res == get_dataset_from_csv("test_data_3.csv", 0)['0']).all() :
      raise Exception('Los resultados obtenidos no coinciden con los esperados (-8%)')
except Exception as e:
  print_function_error('count_nulls_per_column', e)
  grade -= 8

try:
  ds = get_dataset_from_csv("test_dataset.csv", 0)
  res = remove_cols_with_nulls(ds)
  if not (set(res.columns) == { 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year',
                                'Runtime (Minutes)', 'Rating', 'Votes' }) :
    raise Exception('No se eliminaron las columnas esperadas (-8%)')
except Exception as e:
  print_function_error('remove_cols_with_nulls', e)
  grade -= 8

try:
  ds = get_dataset_from_csv("test_dataset.csv", 0)
  res = get_slice(ds, 300, 350)
  test = get_dataset_from_csv("test_data_4.csv", 0)
  if not equal_dataframes(res, test):
    raise Exception('No se obtuvo el dataset esperado (-8%)')
except Exception as e:
  print_function_error('get_slice', e)
  grade -= 8

try:
  ds = get_dataset_from_csv("test_dataset.csv", 0)
  res = filter_by_col(ds, "Genre", "Horror,Thriller")
  test = get_dataset_from_csv("test_data_5.csv", 0)
  if not equal_dataframes(res, test):
    raise Exception('No se obtuvo el dataset esperado (-8%)')
except Exception as e:
  print_function_error('filter_by_col', e)
  grade -= 8

try:
  ds = get_dataset_from_csv("test_dataset.csv", 0)
  res = fill_numeric_nulls(ds)
  test = get_dataset_from_csv("test_data_6.csv", 0)
  if not (res.columns.to_list() == ds.columns.to_list()):
  	raise Exception('El datset retornado no tiene las mismas columnas que el original (-15%)')
  num_test = test.select_dtypes(include="number").to_numpy()
  num_res = res.select_dtypes(include="number").to_numpy()
  if not np.allclose(num_test, num_res):
    raise Exception('No se obtuvo el dataset esperado (-15%)')
except Exception as e:
  print_function_error('fill_numeric_nulls', e)
  grade -= 15

try:
  ds = get_dataset_from_csv("test_dataset.csv", 0)
  res = get_most_correlated_cols(ds, 0.5)
  if not isinstance(res, set):
    raise Exception('No se retorna un objeto de tipo set (-23%)')
  else:
    for i in res:
      if not isinstance(i, frozenset):
        raise Exception('Los elementos de la lista resultantes deben ser tipo frozenset (-23%)')
    if res != { frozenset({'Votes', 'Rating'}), 
                frozenset({'Rating', 'Metascore'}), 
                frozenset({'Votes', 'Revenue (Millions)'})} :
      raise Exception('No se obtuvo las variables esperadas (-23%)')
except Exception as e:
  print_function_error('get_most_correlated_cols', e)
  grade -= 23

end_and_print_grade()