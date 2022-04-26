import pandas as pd

def prep_data(df_list):
    """ Returns a dataframe of the series with the given id."""
    # concat the dataframes
    df = pd.concat(df_list, axis=1)
    # sort the dataframe by date
    df = df.sort_index()
    # convert the index to a dataframe
    df = pd.DataFrame(df)
    # set index to datetime
    df.index = pd.to_datetime(df.index, format='%Y%m')
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '').str.replace('.', '').str.replace('-', '').str.replace(',','')
    return df

def feat_eng(df):
    df['fossil_fuels_difference'] = df['total_fossil_fuels_production_monthly'] - df['total_fossil_fuels_consumption_monthly']
    df['primary_energy_import/export'] = df['total_primary_energy_imports_monthly'] - df['total_primary_energy_exports_monthly']
    df['primary_energy_difference'] = df['total_primary_energy_production_monthly'] - df['total_primary_energy_consumption_monthly']
    df['total_fossil_fuel_difference'] = df['total_fossil_fuels_consumption_monthly'] - df['total_primary_energy_consumption_monthly']
    return df

def fossil_fuels(df):
    df = df[['total_fossil_fuels_production_monthly', 'total_fossil_fuels_consumption_monthly', 'fossil_fuels_difference']]
    return df