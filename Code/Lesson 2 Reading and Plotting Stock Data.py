# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 16:57:34 2018

@author: rcurr
"""

#lesson 2 13 quiz
import pandas as pd
import matplotlib.pyplot as plt

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



#program start
def plot_intraday_high(symbol):
     df = pd.read_csv(dataPath + "{}.csv".format(symbol))
     df["High"].plot()
     plt.show()

def get_mean_volume(symbol):
   df = pd.read_csv(dataPath+"{}.csv".format(symbol))
   return df["Volume"].mean()
   
def get_max_close(symbol):
    df = pd.read_csv(dataPath+"{}.csv".format(symbol))
    return df["Close"].max()

def plot_close_adjclose(symbol):
    df = pd.read_csv(dataPath + "{}.csv".format(symbol))
    df[["Close","Adj Close"]].plot()
    plt.show()

def test_run():
    df = pd.read_csv(path + "Data\\aapl.csv")
    print(df[10:21])
    
def test_run2():
    for symbol in ['AAPL', 'IBM']:
        print("Max Close")
        print(symbol, get_max_close(symbol))
        
def test_run3():
    for symbol in ['AAPL', 'IBM']:
        print("Mean Volume")
        print(symbol, get_mean_volume(symbol))
        
def run():
    for symbol in ['AAPL', 'IBM']:
        plot_close_adjclose(symbol)        
    
if __name__ == "__main__":
    run()