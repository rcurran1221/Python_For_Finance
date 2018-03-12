# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 17:16:04 2018

@author: rcurran
"""

import numpy as np

##14


def get_max_index(a):
    return a.argmax()

def test_run():
    a = np.array([(20,25,10,23,26,32,10,5,0), (0,2,50,20,0,1,28,5,0)])
    print(a)
    
    print(a/2)

if __name__ == "__main__":
    test_run()