import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt 
from statsmodels.tsa.api import Holt



def split_data_model(df):
    df = df.loc[df.index >= '2005']
    train_size = int(len(df) * 0.5)
    validate_size = int(len(df) * 0.3)
    validate_end_index = train_size + validate_size
    train = df[:train_size]
    validate = df[train_size:validate_end_index]
    test = df[validate_end_index:]
    return train, validate, test

def evaluate(target_var, validate, yhat_df):
    '''
    This function will take the actual values of the target_var from validate, 
    and the predicted values stored in yhat_df, 
    and compute the rmse, rounding to 0 decimal places. 
    it will return the rmse. 
    '''
    rmse = round(sqrt(mean_squared_error(validate[target_var], yhat_df[target_var])), 0)
    return rmse


def plot_and_eval(target_var, train, validate, yhat_df):
    '''
    This function takes in the target var name (string), and returns a plot
    of the values of train for that variable, validate, and the predicted values from yhat_df. 
    it will als lable the rmse. 
    '''
    plt.figure(figsize = (12,4))
    plt.plot(train[target_var], label='Train', linewidth=1)
    plt.plot(validate[target_var], label='Validate', linewidth=1)
    plt.plot(yhat_df[target_var])
    plt.title(target_var)
    rmse = evaluate(target_var, validate, yhat_df)
    print(target_var, '-- RMSE: {:.0f}'.format(rmse))
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Production (MtCO2)')
    plt.show()
    return


# def append_eval_df(model_type, target_var):
#     '''
#     this function takes in as arguments the type of model run, and the name of the target variable. 
#     It returns the eval_df with the rmse appended to it for that model and target_var. 
#     '''
#     rmse = evaluate(target_var)
#     d = {'model_type': [model_type], 'target_var': [target_var],
#         'rmse': [rmse]}
#     d = pd.DataFrame(d)
#     return eval_df.append(d, ignore_index = True)

# Simple Average
def compute_simple_average(train):
     production = round(train['total_fossil_fuels_production_monthly'].mean(), 2)
     consumption = round(train['total_fossil_fuels_consumption_monthly'].mean(), 2)
     return production, consumption

def make_predictions(production, consumption, validate):
     yhat_df = pd.DataFrame({'total_fossil_fuels_production_monthly': [production],
                            'total_fossil_fuels_consumption_monthly': [consumption],},
                            index=validate.index)
     return yhat_df

# def simple_average(train, validate):
#     production, consumption, difference = compute_simple_average(train)
#     yhat_df = make_predictions(production, consumption, difference, validate)
#     for col in train.columns:
#         plot_and_eval(col, train, validate, yhat_df)
    # return

# Holt's model

def holts_15_12_model(train, validate):
    production, consumption = compute_simple_average(train)
    yhat_df = make_predictions(production, consumption, validate)
    yhat_df
    for col in train.columns:
        model = Holt(train[col], exponential=False)
        model = model.fit(smoothing_level=0.15, smoothing_slope=0.12, optimized=False)
        yhat_items = model.predict(start = validate.index[0], end= validate.index[-1])
        yhat_df[col] = round(yhat_items, 2)
    train.rename(columns={'total_fossil_fuels_production_monthly': 'Holts 15/12 model achieved a RMSE score of 364.'}, inplace=True)
    train.rename(columns={'total_fossil_fuels_consumption_monthly': 'Holts 15/12 model achieved a RMSE score of 645.'}, inplace=True)
    validate.rename(columns={'total_fossil_fuels_production_monthly': 'Holts 15/12 model achieved a RMSE score of 364.'}, inplace=True)
    validate.rename(columns={'total_fossil_fuels_consumption_monthly': 'Holts 15/12 model achieved a RMSE score of 645.'}, inplace=True)
    yhat_df.rename(columns={'total_fossil_fuels_production_monthly': 'Holts 15/12 model achieved a RMSE score of 364.'}, inplace=True)
    yhat_df.rename(columns={'total_fossil_fuels_consumption_monthly': 'Holts 15/12 model achieved a RMSE score of 645.'}, inplace=True)

    for col in train.columns:
        plot_and_eval(col, train, validate , yhat_df)
    return yhat_df

# previous_year model

def previous_year(df):
    #split
    train = df['2004':'2010']
    validate = df['2011':'2016']
    # make yhat_df
    yhat_df = train['2005':'2010'] + train.diff(60).mean()
    # concat dataframes
    pd.concat([yhat_df.head(1), validate.head(1)])
    # set yhat_df to index of validate
    yhat_df.index = validate.index
    
    train.rename(columns={'total_fossil_fuels_production_monthly': 'Previous year model achieved a RMSE score of 648.'}, inplace=True)
    train.rename(columns={'total_fossil_fuels_consumption_monthly': 'Previous year model achieved a RMSE score of 372.'}, inplace=True)
    validate.rename(columns={'total_fossil_fuels_production_monthly': 'Previous year model achieved a RMSE score of 648.'}, inplace=True)
    validate.rename(columns={'total_fossil_fuels_consumption_monthly': 'Previous year model achieved a RMSE score of 372.'}, inplace=True)
    yhat_df.rename(columns={'total_fossil_fuels_production_monthly': 'Previous year model achieved a RMSE score of 648.'}, inplace=True)
    yhat_df.rename(columns={'total_fossil_fuels_consumption_monthly': 'Previous year model achieved a RMSE score of 372.'}, inplace=True)

    for col in train.columns:
        plot_and_eval(col, train, validate, yhat_df)
    return

# conclustion model

def final_plot(target_var, train, validate, test, yhat_df):
    plt.figure(figsize=(12,4))
    plt.plot(train[target_var], label='train')
    plt.plot(validate[target_var], label='validate')
    plt.plot(test[target_var], label='test')
    plt.plot(yhat_df[target_var], alpha=.5)
    plt.title(target_var)
    plt.xlabel('Year')
    plt.ylabel('Production (MtCO2)')
    plt.legend()
    plt.show()

def conclusion_model(df):
    train = df['2004':'2010']
    validate = df['2011':'2016']
    test = df['2016':'2021']
    #train + validate to predict test
    yhat_df = validate + train.diff().mean()
    yhat_df.index = test.index

    train.rename(columns={'total_fossil_fuels_production_monthly': 'Holts 15/12 model utilized on Out-of-Sample data.'}, inplace=True)
    train.rename(columns={'total_fossil_fuels_consumption_monthly': 'Previous year model utilized on Out-of-Sample data.'}, inplace=True)
    validate.rename(columns={'total_fossil_fuels_production_monthly': 'Holts 15/12 model utilized on Out-of-Sample data.'}, inplace=True)
    validate.rename(columns={'total_fossil_fuels_consumption_monthly': 'Previous year model utilized on Out-of-Sample data.'}, inplace=True)
    test.rename(columns={'total_fossil_fuels_production_monthly': 'Holts 15/12 model utilized on Out-of-Sample data.'}, inplace=True)
    test.rename(columns={'total_fossil_fuels_consumption_monthly': 'Previous year model utilized on Out-of-Sample data.'}, inplace=True)
    yhat_df.rename(columns={'total_fossil_fuels_production_monthly': 'Holts 15/12 model utilized on Out-of-Sample data.'}, inplace=True)
    yhat_df.rename(columns={'total_fossil_fuels_consumption_monthly': 'Previous year model utilized on Out-of-Sample data.'}, inplace=True)

    for col in train.columns:
        final_plot(col,train, validate, test, yhat_df)
    return 

def prediction_model(df):
    train = df['2004':'2010']
    validate = df['2011':'2016']
    test = df['2016':'2021']
    # to predict the next six years
    yhat_df = test + train.diff(60).mean()
    yhat_df.index = test.index + pd.Timedelta('6Y')

    train.rename(columns={'total_fossil_fuels_production_monthly': '2022-2028 fossil fuel production will increase at unsure patterns.'}, inplace=True)
    train.rename(columns={'total_fossil_fuels_consumption_monthly': '2022-2028 fossil fuel consumtion will continue to decrease.'}, inplace=True)
    validate.rename(columns={'total_fossil_fuels_production_monthly': '2022-2028 fossil fuel production will increase at unsure patterns.'}, inplace=True)
    validate.rename(columns={'total_fossil_fuels_consumption_monthly': '2022-2028 fossil fuel consumtion will continue to decrease.'}, inplace=True)
    test.rename(columns={'total_fossil_fuels_production_monthly': '2022-2028 fossil fuel production will increase at unsure patterns.'}, inplace=True)
    test.rename(columns={'total_fossil_fuels_consumption_monthly': '2022-2028 fossil fuel consumtion will continue to decrease.'}, inplace=True)
    yhat_df.rename(columns={'total_fossil_fuels_production_monthly': '2022-2028 fossil fuel production will increase at unsure patterns.'}, inplace=True)
    yhat_df.rename(columns={'total_fossil_fuels_consumption_monthly': '2022-2028 fossil fuel consumtion will continue to decrease.'}, inplace=True)

    for col in train.columns:
        final_plot(col,train, validate, test, yhat_df)