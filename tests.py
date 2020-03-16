import pandas as pd

def get_dataset_from_csv(filename, index_col_num):
  """Retorna un DataFrame leyendolo desde el archivo <filename>, define la columna en la posicion <index_col_num> como índice de éste."""
  path = filename
  df = pd.read_csv(path, index_col = index_col_num)

  return df

tmp = get_dataset_from_csv('test_data_1.csv', 0)
print(tmp)