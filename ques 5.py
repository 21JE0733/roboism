# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RZIhdXD1xYu8cR-3aBSftpAysp126F94
"""

import numpy
from numpy import random
x=random.randint(99, size=(100))
print(x)
a = 0
for i in range(0,len(x)):
  for j in range(i+1,len(x)):
    if(x[i]==x[j]):
      print(x[i])
      a += 1
      break
    if(a!=0):
      break