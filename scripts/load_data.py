
import pandas as pd


def data_loader(file_path):
    try:
         df = pd.read_csv(file_path, delimiter='|')
    except Exception as e:
         print(f'Error {e}')
    
    return df

        