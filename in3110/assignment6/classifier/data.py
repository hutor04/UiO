import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt


def prepare_data(inputfile: str):
    """
    Reads input csv file into Pandas dataframe. Removes rows where one of the values is NaN. Removes the first column
    which is just a serial number of the row. Converts 'Diabetes' column to int, where 1 stands for positive,
    0 standa for negative.
    Splits the data frame into training and test sets, where training set is 80% of data.
    The proportion of values in 'diabetes' column is preserved both in the training and
    test sets
    :param inputfile: string, Path to the input file
    :return: tuple of DataFrames, Training and test data sets.
    """
    pima_DF = pd.read_csv(inputfile)
    pima_DF = pima_DF.dropna()
    pima_DF = pima_DF.drop(pima_DF.columns[0], axis=1)
    pima_DF['diabetes'].replace(to_replace=['pos'], value='1', inplace=True)
    pima_DF['diabetes'].replace(to_replace=['neg'], value='0', inplace=True)
    pima_DF['diabetes'] = pd.to_numeric(pima_DF['diabetes'])
    train, test = train_test_split(pima_DF, test_size=0.2, stratify=pima_DF['diabetes'])
    return train, test


def draw_scatter_plot(df, feature_1, feature_2):
    """
    Takes in the dataframe, and two feature names and draws a scatter plot. The color depends on the class.
    I.e. diabetes detected or not.
    :param df: Pandas DF Data sources
    :param feature_1: str Feature name
    :param feature_2: str Feature name
    :return:
    """
    sns.lmplot(x=feature_1, y=feature_2, data=df, fit_reg=False, hue='diabetes', legend=True)
    plt.show()


if __name__ == '__main__':
    train, test = prepare_data('./static/diabetes.csv')
    draw_scatter_plot(train, 'pregnant', 'glucose')
    draw_scatter_plot(train, 'pressure', 'triceps')
