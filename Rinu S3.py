#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:50:26 2022

@author: sjcet
"""
import numpy as np
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print("x=",x)
print("y=",y)
print("Transpose of the matrix x")
print(x.transpose())
print("Transpose of the matrix y")
print(y.transpose())
print("Matrix addition")
print(np.add(x,y))