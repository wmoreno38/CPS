import pandas as pd

def load_data():
    df = pd.read_csv('titanic.csv')
    print(df.describe())

if __name__ == '__main__':
    load_data()
