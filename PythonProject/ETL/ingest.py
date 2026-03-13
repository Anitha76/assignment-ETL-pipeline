import pandas as pd

def load_data():

    file_path = r"C:\Users\hr345\PycharmProjects\PythonProject\sourceData\raw\cleaned_dataset.csv"

    df = pd.read_csv(file_path)

    print("Data loaded successfully")
    print("Total records:", len(df))
    # print(df.columns)

    return df


#
# if __name__ == "__main__":
#     load_data()