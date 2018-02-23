# file for providing validation test data sources and visualization. Creation date wk 1808.5
# run with python -i


# import libraries:
import numpy as np
import matplotlib.pyplot as plt
import pylab

fig = plt.figure()


def test1(dvar, dvar2, dlen, davg): #input parameters
	#generate random signal
	plt.figure(1)

	noise = np.random.normal(davg,dvar,dlen)	
	noise2 = np.random.normal(davg,dvar2,dlen)
	# 0 is the mean of the normal distribution you are choosing from
	# 1 is the standard deviation of the normal distribution
	# 100 is the number of elements you get in array noise

	#update noise 
	noise = np.append(noise, noise2)

	#use gr to plot function
	plt.plot(noise)
	plt.show()

# init
dvar = 0.1 #variance 1
dvar2 = 0.2 #variance 2
dlen = 1000 #length of time-series signal
davg = 0 #average of timeseries signal

# test1 
test1(dvar, dvar2, dlen, davg)