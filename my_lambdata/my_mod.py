
# my_lambdata/my_mod.py

import pandas as pd
from sklearn.model_selection import train_test_split
from scipy import stats
import numpy as np
import random

class Df_fancy():

    def __init__(self, df):
        self.df = df
        
    
    def set_train_val_test(self, random_state = 42):
        """
        Returns train, validation, and test sets
        """
        train, test = train_test_split(self.df, random_state = random_state)
        train, val = train_test_split(train, random_state = random_state)
        return train, val, test
    
    def generate_data(self, rows_to_add, random_state=42):
        """
        Param rows_to_add is an int that specifies the new number of rows to add
        """
        rows = []
        for i in range(0, len(self.df.columns)-1):
            rows.append([])
        for row in range(0,rows_to_add):
            for col in self.df.columns.tolist():
                rows[row].append(random.choices(np.unique(self.df[col]).tolist()))
        temp_df = pd.DataFrame(rows, columns=['target','cat1','cat2'])
        print(self.df.head())
        print(temp_df.head())
        self.df = pd.concat([self.df, temp_df])
        return self.df
        

    # def set_chi_2_report(self, cat1, cat2):
    #     """
    #     Param cat1 is a categorical variable
    #     Param cat2 is another categorical variable
    #     Returns a contingency table and a chi squared test
    #     """
    #     self.contingency_table = pd.crosstab(self.df[cat1], self.df[cat2])
    #     self.chi2_test = stats.chi2_contingency(contingency_table)
    #     return self.contingency_table, self.chi2_test

    # def get_contingency(self):
    #     """
    #     Returns contingency table for cat 1 and 2
    #     """
    #     return self.contingency_table

    # def get_chi2(self):
    #     """
    #     Returns chi2 table for cat 1 and 2
    #     """
    #     return self.chi2

    # def get_chi2_report(self):
    #     """
    #     Returns contingency table and chi2 table for at 1 and cat 2
    #     """
    #     return self.contingency_table, self.chi2


# An example function
def enlarge(n):
    """
    Param n is a number
    Function will return enlarge the number
    """
    return n * 100


# def train_val_test_split(df, random_state=42):
#     """
#     Param df is a dataframe
#     Function will retun a train, validate, test split with default sizes
#     """
#     train, test = train_test_split(df)
#     train, val = train_test_split(train)

#     return train, val, test


# def chi_2_report(df, a, b):
#     """
#     Param df is a dataframe
#     Param a is a categorical variable
#     Param b is a categorical variable
#     Function will return a contingnecy table and a chi squared test
#     """
#     contingency_table = pd.crosstab(df[a], df[b])
#     return contingency_table, stats.chi2_contingency(contingency_table)
