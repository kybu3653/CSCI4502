#! usr/bin/python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#sorry I couldn't get audio working
#this reads in the command line
assert(len(sys.argv)==2)
attr = int(sys.argv[1])-1  #sub 1 because of indexing
assert(attr>=0 and attr<=9)

#read in data file
df = pd.read_csv('magic04.data',names=np.arange(11))

#quantiles
A = df[attr]
Q1 = A.quantile(.25)
Q3 = A.quantile(.75)

print A.count(), A.min(), A.max(),A.mean(),A.std(),Q1,A.median(), Q3, Q3-Q1 

#this generates plot 
x  = [elements for elements in df[3]]
y = [items for items in df[4]]
plt.scatter(x,y)
plt.xlabel("Attribute 4")
plt.ylabel("Attribute 5")
plt.title("Heteroscadastic Plot")
plt.show()

