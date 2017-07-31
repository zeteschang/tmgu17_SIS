#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:03:03 2017

@author: iRomix
"""

# import all modules in beginning of text
import glob, io, os, re
wd = '/Users/iRomix/Desktop/YTScraper/Com_BC/'
os.chdir(wd)

"""
##option with numpy

import numpy
dir(numpy)# list of functions in numpy
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

print type(data)
print data.dtype
print data.shape
print data

print 'first value is:', data[0,0]

print data[0,0],data[0,1],data[0,2],data[0,3]
print 'is the same as:'
print data[0,0:4]

## slicing a numpy array (or matrix)
print data[0,0:4]# slicing columns
print data[0:4,0]# slicing rows
print data[0:4,0:4]# slicing rows and columns

var = data[0,0:10]# assign slice to variable
print var


#option 1 with pandas
import pandas as pd
df=pd.read_csv('commovie.csv', sep=',',header=None)
df.values
"""

#option 2 "
import pandas as pd
comcam = pd.read_csv('commovie.csv', sep = ',')
comcam.head()

df = pd.DataFrame(comcam, columns=['date', 'commentText']) 
print df
df.head()
df.tail()

print df[:100]

df.dropna() 



