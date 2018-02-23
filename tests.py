# file for providing validation test data sources and visualization. Creation date wk 1808.5

# import libraries:
import numpy as np
from gr import pygr


#input parameters
dvar = 10 #variance
dlen = 10 #length of time-series signal
damp = 10 #amplitude of time series signal

#change at t = x
t_change = 10

#generate random signal

noise = np.random.normal(0,1,100)

# 0 is the mean of the normal distribution you are choosing from
# 1 is the standard deviation of the normal distribution
# 100 is the number of elements you get in array noise

pygr.plot(list(x**2 for x in range(100)))