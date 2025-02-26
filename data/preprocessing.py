import pandas as pd
import numpy as np

data = pd.read_csv("data/hotelData.csv")

def drop_rows(df):
    # df = df.dropna(how = "any", axis = 0)
    # df = df.loc[(df != 0).all(axis=1)]
    # df = df.loc[~(df=='0').all(axis=1)]
    df = df.replace(0, np.nan).dropna(how = "any", axis = 0)
    return df


def combine_columns(df):
    pass

if __name__ == "__main__":
    new_df = drop_rows(df = data)
    data = data.replace(0, np.nan).dropna(how = "any", axis = 0)
    print(new_df.head())
    print(len(new_df))
    print(data.loc[1092])
