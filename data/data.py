import pandas as pd


def save_data(data):
    path = "./data/file" + str(len(data)) + ".csv"
    pd.DataFrame(data).to_csv(path)
    print("Saved data into file named - " + "file " + str(len(data)))
