# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 16:09:23 2018

@author: rcurran
"""

import pandas as pd
import os
#where is the data?
atWork = 1

rcurranRepoPath = "C:\\Users\\rcurran\\Python\\Python_For_Finance\\"
rcurrRepoPath = "C:\\Users\\rcurr\\Python_For_Finance\\"

if (atWork == 1):
    path = rcurranRepoPath
else:
    path = rcurrRepoPath
    
dataPath = path + "data\\"
#endregion

def symbol_to_path(symbol):
    return os.path.join(dataPath, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    df = pd.DataFrame(index = dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')
        
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col = 'Date', 
                    parse_dates = True, usecols = ['Date', 'Adj Close']
                    ,na_values = ['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close' : symbol })
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset = ["SPY"])
    
    return df
    
def test_run0():
    start_date = '2016-01-22'
    end_date = '2016-01-28'
    dates = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index=dates)
    
    dfSPY = pd.read_csv(dataPath + "SPY.csv", index_col = 'Date',
                       parse_dates = True, usecols = ['Date', 'Adj Close'],
                       na_values = ['nan'])
    dfSPY = dfSPY.rename(columns = {'Adj Close' : 'SPY'})
    
    #left join is default
    df1 = df1.join(dfSPY, how = 'inner')
    
    symbols = ['AAPL', 'GLD', 'GOOG', 'IBM'] #, 'SPY']
    for symbol in symbols:
        df_temp = pd.read_csv(dataPath + "{}.csv".format(symbol), 
                              index_col = 'Date',
                              parse_dates = True, usecols = ['Date', 'Adj Close']
                              ,na_values = ['nan'])
        
        df_temp = df_temp.rename(columns = {'Adj Close' : symbol})
        df1 = df1.join(df_temp)
    print(df1)
        
def test_run():
    dates = pd.date_range('2017-01-20', '2017-01-28')
    
    symbols = ['GOOG', 'IBM', 'GLD', 'AAPL']
    df = get_data(symbols, dates)
    print (df)
        
if __name__ == "__main__":
    test_run()
    
    #lesson 3 obtaining a slice of data