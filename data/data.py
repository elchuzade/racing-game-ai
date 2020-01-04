import pandas as pd


def save_data(data):
    path = "./file" + len(data) + ".csv"
    pd.DataFrame(data).to_csv(path)
