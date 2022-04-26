import pandas as pd
import requests
import env

def epi_category(category_id):
    """ Returns the name of the category with the given id. Initial id key is  711238"""
    key = env.api_key
    url = 'https://api.eia.gov/category/?api_key=' + key + '&category_id=' + category_id
    result = requests.get(url)
    result.status_code
    result.json()
    return result.json()

def data_manipulation(data):
    """ Returns a dataframe of the series with the given id."""
    # convert to dataframe to view data i would like to view
    df_series = pd.DataFrame(data['category']['childseries'])
    df_series
    # select only the f rows that have 'A'
    df_series[df_series['f'] == 'A']
    series_id = []
    series_name = []
    for i in range(len(df_series)):
        if df_series['f'][i] == 'M':
            series_id.append(df_series['series_id'][i])
            series_name.append(df_series['name'][i])
    print(series_id)
    print(series_name)
    return series_id, series_name

    # create a function that turns the data into a dataframe
def build_df(series_id):
    """ Returns a dataframe of the series with the given id."""
    data = epi_series(series_id)
    df = pd.DataFrame(data['series'])
    # seperate the 'data'
    df_dict = df['data'].to_dict()
    # convert to dataframe
    # df_data = pd.DataFrame(df_dict)
    # convert to list
    # df_dict[0].tolist()
    # convert list to dataframe
    df = pd.DataFrame(df_dict[0])
    df.columns = ['date', 'value']
    return df

    # create a function that takes in a list of series_id and names and builds a dataframe from the data for each series_id properly naming the values
def build_df_list_rename(series_id_list, series_name_list):
    """ Returns a dataframe of the series with the given id."""
    df_list = []
    for series_id, series_name in zip(series_id_list, series_name_list):
        df = build_df(series_id)
        df.rename(columns={'value': series_name}, inplace=True)
        # join the dataframes using the date as the index
        df = df.set_index('date')
        df_list.append(df)
    return df_list

def epi_series(category_id):
    """ Returns the name of the category with the given id."""
    url = 'https://api.eia.gov/series/?api_key=9eVTCpuQVgMQDZnriiK5gt3uNzwJMzzf4dBzvE2s&series_id=' + category_id
    result = requests.get(url)
    result.status_code
    result.json()
    return result.json()

