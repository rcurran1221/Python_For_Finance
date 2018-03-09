# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 17:16:04 2018

@author: rcurran
"""

import numpy as np
import time

##14

def test_run():
    nd1 = np.random.random((1000, 10000))
    
    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    print("Manual: {:.6f} ({:.3f} secs.) vs Numpy: {:.6f} ({:.3f} secs.)".format()))


#def get_max_index(a):
#    return a.argmax()
#
##def test_run():
#  
#    np.random.seed(693)
#    a = np.random.randint(0, 10, size=(5,4))
#    print("Array:\n", a)
#    
#    print("Maximum value:", a.max())
#    print("Index of max.:", get_max_index(a))

if __name__ == "__main__":
    test_run()