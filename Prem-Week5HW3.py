# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 18:40:02 2018

@author: sagarprem
Author : PREM SAGAR
"""

# Import pandas
import pandas as pd
import numpy as np
import os
#import matplotlib.pyplot as plt

def readCSV():
    path = input("Enter Full CSV file path:  ")
    os.chdir(path)
    os.listdir('.')
    filename = input("Enter Full CSV filename:  ")

    # Load spreadsheet
    df_csv_data = pd.read_csv(filename)
    
    arg_perc = input("Enter Value of Percentage:  ")
    
    percentile = np.percentile(df_csv_data,arg_perc)
    print(percentile)
    
readCSV()