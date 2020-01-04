import pandas as pd


def write_data(data):
    path = "./file" + str(len(data)) + ".csv"
    pd.DataFrame(data).to_csv(path)
