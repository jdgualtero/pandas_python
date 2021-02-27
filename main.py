from txt import pandas_txt 


def main():
    pandas_txt.read_dict_pandas_to_file()
    pandas_txt.read_file_pandas("example_dataframe_to_csv.csv", ",")

main()