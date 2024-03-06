import os

import opendatasets as od
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from config import dataset, path, prepared_path


def grab_col_names(dataframe, cat_th=10, car_th=20, dump_info=False):
    """ """
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [
        col
        for col in dataframe.columns
        if dataframe[col].nunique() < cat_th and dataframe[col].dtypes != "O"
    ]
    cat_but_car = [
        col
        for col in dataframe.columns
        if dataframe[col].nunique() > car_th and dataframe[col].dtypes == "O"
    ]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    #  Number Columns
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]
    num_cols = [col for col in num_cols if dataframe[col].nunique() != len(dataframe)]

    if dump_info:
        print(f"Observations: {dataframe.shape[0]}")
        print(f"Variables: {dataframe.shape[1]}")
        print(f"cat_cols: {len(cat_cols)}")
        print(f"num_cols: {len(num_cols)}")
        print(f"cat_but_car: {len(cat_but_car)}")
        print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car


#  Download
od.download(dataset)

#  EDA
df = pd.read_csv(path)

choose_list = [
    "Brokertitle",
    "Address",
    "State",
    "Main_address",
    "Administrative_area_level_2",
    "Sublocality",
    "Street_name",
    "Long_name",
    "Formatted_address",
    "Longitude",
    "Latitude",
]
choose_list = [col.upper() for col in choose_list]

df.drop(choose_list, axis=1, inplace=True)

cat_cols, num_cols, cat_but_car = grab_col_names(df)
drop_first = False
df = pd.get_dummies(df, columns=cat_cols, drop_first=drop_first)

#  Scale

scaler = MinMaxScaler()
df[num_cols] = pd.DataFrame(
    scaler.fit_transform(df[num_cols]), columns=df[num_cols].columns
)

ext_dir = os.path.dirname(os.path.abspath(prepared_path))
if not os.path.exists(ext_dir):
    os.mkdir(ext_dir)

df.to_csv(prepared_path)
