# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 16:09:23 2018

@author: rcurran
"""
import matplotlib.pyplot as plt
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

#public properties
symbols = ['AAPL', 'GLD', 'GOOG', 'IBM']
Start_Date = '2017-01-01'
End_Date = '2017-12-31'
Df_Date_Range = pd.date_range(Start_Date, End_Date)
#endregion

def symbol_to_path(symbol):
    return os.path.join(dataPath, "{}.csv".format(str(symbol)))

def plot_selected(df, columns, start_index, end_index):
    df = df.ix[start_index : end_index, columns]
    plot_data(df, title = "Selected prices")

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
    
def plot_data(df, title="Stock prices"):
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date") 
    ax.set_ylabel("Price")
    plt.show()
    
def normalize_data(df):
    return df/df.ix[0,:]
    
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
    
     #, 'SPY']
    for symbol in symbols:
        df_temp = pd.read_csv(dataPath + "{}.csv".format(symbol), 
                              index_col = 'Date',
                              parse_dates = True, usecols = ['Date', 'Adj Close']
                              ,na_values = ['nan'])
        
        df_temp = df_temp.rename(columns = {'Adj Close' : symbol})
        df1 = df1.join(df_temp)
    print(df1)
        
def test_run1():
    dates = pd.date_range('2017-01-01', '2017-12-31')
    
    symbols = ['GOOG', 'IBM', 'GLD', 'AAPL']
    df = get_data(symbols, dates)
    df = df.ix['2010-01-01':'2017-01-31', symbols]
    df = df/df.ix[0]
    df.plot()
    
def test_run2():
    df = get_data(symbols, Df_Date_Range)
    plot_data(df)
        
def test_run3():
    plot_selected(get_data(symbols, Df_Date_Range), ['SPY', 'GLD'], Start_Date, End_Date)
    
def test_run():
    df = normalize_data(get_data(symbols, Df_Date_Range))
    plot_data(df)

if __name__ == "__main__":
    test_run()
    
    
    #lesson 3 obtaining a slice of data