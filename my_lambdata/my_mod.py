
# my_lambdata/my_mod.py

import pandas as pd
from sklearn.model_selection import train_test_split
from scipy import stats

# An example function
def enlarge(n):
    """
    Param n is a number
    Function will return enlarge the number
    """
    return n * 100

def train_val_test_split(df,random_state=42):
    """
    Param df is a dataframe
    Function will retun a train, validate, test split with default sizes
    """
    train, test = train_test_split(df)
    train, val = train_test_split(train)

    return train, val, test

def chi_2_report(df,a,b):
    """
    Param df is a dataframe
    Param a is a categorical variable
    Param b is a categorical variable
    Function will return a contingnecy table and a chi squared test
    """
    contingency_table = pd.crosstab(df[a],df[b])
    return contingency_table, stats.chi2_contingency(contingency_table)
    