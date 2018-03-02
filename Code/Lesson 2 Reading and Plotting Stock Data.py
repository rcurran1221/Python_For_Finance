# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 16:57:34 2018

@author: rcurr
"""

#lesson 2 section 9 selecting rows
import pandas as pd

def test_run():
    df = pd.read_csv(r'C:\Users\rcurr\Python\Python_For_Finance\Data\aapl.csv')
    print(df.head())
    
if __name__ == "__main__":
0    test_run()