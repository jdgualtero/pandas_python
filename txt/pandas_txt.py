import pandas as pd

import numpy as np 

def read_dict_pandas_to_file():
    dict_example = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
                    'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
                    'age': [27, 31, 36, 53, 48, 36, 40, 34],
                    'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
                    'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
                    }
    data_frame = pd.DataFrame(dict_example, columns= ['first_name', 'last_name', 'age', 'amount_1', 'amount_2'])

    name_file_example = "example_dataframe_to_csv.csv"

    data_frame.to_csv(name_file_example)

    print(f"file {name_file_example} created.")

    read_dict_pandas_to_file


def read_file_pandas(file_name, sep):
    
    file_data_frame = None

    if sep != None:
       file_data_frame = pd.read_csv(file_name)
    else:
        file_data_frame = pd.read_csv(name_file_example,sep)
    print(" ==== DATA FRAME ==== ")
    print(file_data_frame)

    df_result = file_data_frame[["first_name","first_name"]]

    print()
    print()
    print(" ===== Data filtered =====")
    print()
    print()
    print(df_result)

    df_result_age = file_data_frame["age"] > 30
    
    print()
    print()
    print(" ===== Data filtered =====")
    print()
    print()
    print(file_data_frame[df_result_age])

