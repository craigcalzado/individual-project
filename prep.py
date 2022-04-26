import pandas as pd

# create a function that prepares the data
def prepare_data(df_list):
    df_list.index = pd.to_datetime(df_list.index, format='%Y%m')
    df_list.columns = df_list.columns.str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '').str.replace('.', '').str.replace('-', '').str.replace(',','')
    return df_list