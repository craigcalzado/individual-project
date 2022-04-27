import matplotlib.pyplot as plt
import seaborn as sns

def explore_split(df):
    """
    Explores the dataframe and splits it into a training and testing set.
    """
    # split the dataframe into a training and testing set
    train = df.loc['2005':'2014'] # includes 2010
    test = df.loc['2015':'2021']

    plt.plot(train.index, train.total_fossil_fuels_production_monthly)
    plt.plot(test.index, test.total_fossil_fuels_production_monthly)
    # add labels
    plt.xlabel('Date')
    plt.ylabel('Production (MtCO2)')
    plt.title('Shows the distribution of the data split for exploration.')
    plt.show()
    return train, test

def box_plots(train):
    """
    Creates a box plot for the dataframe.
    """
    # create new column for the month name
    train['month'] = train.index.month_name()
    # create a box plot for the month production
    sns.boxplot(data=train, y='total_fossil_fuels_production_monthly', x='month')
    # rotate x-axis labels
    plt.xticks(rotation=45)
    # add labels
    plt.xlabel('Month')
    plt.ylabel('Fossil Fuels Production (Million BTU)')
    plt.title('The porduction of fossil fuels per month in the US')
    plt.show()
    # box plot consumption
    sns.boxplot(data=train, y='total_fossil_fuels_consumption_monthly', x='month')
    # rotate x-axis labels
    plt.xticks(rotation=45)
    # add labels
    plt.xlabel('Month')
    plt.ylabel('Fossil Fuels Consumption (Million BTU)')
    plt.title('The consumption of fossil fuels per month in the US')
    plt.show()
    return

def line_plots(train):
    """
    Creates a line plot for the dataframe.
    """
    # create vaiables for ease of plotting
    y = train.total_fossil_fuels_production_monthly
    x = train.total_fossil_fuels_consumption_monthly
    # create line plot
    y.plot(alpha=.2, label='Monthly')
    y.resample('3M').mean().plot(alpha=.5, label='Tri-Monthly')
    y.resample('6M').mean().plot(alpha=.8, label='Bi-Yearly')
    y.resample('Y').mean().plot(label='Yearly')
    y.resample('5Y').mean().plot(label='Bi-Decade')
    plt.legend()
    # add labels
    plt.xlabel('Date')
    plt.ylabel('Production (MtCO2)')
    plt.title('The production of fossil fuels increases with time exponentially.')
    plt.show()
    x.plot(alpha=.2, label='Monthly')
    x.resample('3M').mean().plot(alpha=.5, label='Tri-Monthly')
    x.resample('6M').mean().plot(alpha=.8, label='Bi-Yearly')
    x.resample('Y').mean().plot(label='Yearly')
    x.resample('5Y').mean().plot(label='Bi-Decade')
    plt.legend()
    # add labels
    plt.xlabel('Date')
    plt.ylabel('Consumption (MtCO2)')
    plt.title('Fossil fuel consumption is at a steady decline.')
    return