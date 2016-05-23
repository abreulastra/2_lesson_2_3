# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:12:42 2016

@author: AbreuLastra_Work
"""

#Importing libraries
from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

#Loading database
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.dropna(inplace=True)

#Estimating the frequency for every value
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

#Ploting a histogram with the frequencies
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)


#Estimaiting the chi-squared statistic
chi, p = stats.chisquare(freq.values())

# Print chi-squared text
print("The chi-squared value for this distribution is %f" % chi)
print("The p-value is %f" % p)