# 18136_arima_and_dataset.py

# import packages

import warnings
import itertools
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = sm.datasets.co2.load_pandas()

y = data.data

#The 'MS' string groups the data in buckets by start of month
y = y['co2'].resample('MS').mean()

#The tem bfill means that we use the value before filling in misisng values
y = y.fillna(y.bfill())
# plt.ion()
# y.plot(figsize=(15,6))
# plt.show()


## ARIMA PART  :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ARIMA function takes parameters p, d, q
# p = auto regressive part, incorporate effect of past values in model
# d = intregrates the amount of differencing in the model
# q = moving average part of the model, set error of model as linear combination of error values
# 		observed at previous time points in past
# use 'grid search' method of assesing of searchin parameters for ARIMA

# P, D, Q take into account Seasonal effects

# SARIMAX function of statsmodels module is used to assess its overal quality

# take any range between 0 and 2
p = d = q = range(0,2)

# list all different combinations of p, d, q (integers)
pdq = list(itertools.product(p,d,q))

# gnenerate seasonal combinations of p, d, q
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

# Find model with lowest AIC value (Akaike Information Criterion), basically goodness of fit v.s.
# model complexity... if a complex model has good fit it will be assigned lower score than simple
# model

# Loop through pdq vals:

# AWESOME!!!
warnings.filterwarnings("ignore") # specify to ignore warning messages
# only run analysis when required
runanalysis = False
if runanalysis == True:
	for param in pdq:
	    for param_seasonal in seasonal_pdq:
	        try:
	            mod = sm.tsa.statespace.SARIMAX(y,
	                                            order=param,
	                                            seasonal_order=param_seasonal,
	                                            enforce_stationarity=False,
	                                            enforce_invertibility=False)

	            results = mod.fit()

	            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
	        except:
	            continue

# winning algo (from previous block ^)
# SARIMAX(1,1,1)x(1,1,1,12)- AIC:277.78

# plug optimal parameters in SARIMAX:
mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()
print(results.summary().tables[1])
print("AIC score:")
#Verify AIC
print('ARIMA{}x{}12 - AIC:{}'.format((1, 1, 1), (1, 1, 1, 12), results.aic))


# Plot diagnostics
results.plot_diagnostics(figsize=(15, 12))
plt.show()

# Our primary concern is to ensure that the residuals of our model are uncorrelated and 
# normally distributed with zero-mean. If the seasonal ARIMA model does 
# not satisfy these properties, it is a good indication that it can be further improved.