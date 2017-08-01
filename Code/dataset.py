#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:41:53 2017

@author: iRomix
"""

# import all modules in beginning of text
import glob, io, os, re
wd = 'C:\Users\zdwgh\Desktop\\tmgu_17'
os.chdir(wd)

#libraries
import glob
import numpy as np #we load numpy as np, so we can call the library using np instead of np
import pandas as pd

path ='C:\Users\zdwgh\Desktop\\tmgu_17' #here we define the path
allFiles = glob.glob('C:\Users\zdwgh\Desktop\\tmgu_17\\' + "commovie.json")
frame = pd.DataFrame() #here we initialize a Pandas DataFrame
list_ = []
for file_ in allFiles:
    frame = pd.read_json(file_) #since the files are in json format we use read_json. Other options include read_csv
    list_.append(frame) 
df = pd.concat(list_)

df = pd.DataFrame(frame, columns=['timestamp', 'commentText']) 

print df

#the function to_datetime tells Pandas that the column includes dates
df['timestamp'] = pd.to_datetime(df['timestamp']) 

#the function set_index tells Pandas to use the 'date' column as the index. 
#By specifying the drop parameter as 'False' we tell Pandas to keep the original column with the dates. 
#Otherwise this column is removed. Since we need it for the Second Approach, we want to keep it. 
df = df.set_index(['timestamp'], drop=False)


print df

""" FOR single date variables of timestamp
df['day'] = df['timestamp'].dt.day
df['month'] = df['timestamp'].dt.month
df['year'] = df['timestamp'].dt.year
print df
"""

df.head() #this shows the first lines (put a number between the parenthesis to determine how many lines)
df.tail()



#calculate length of articles
#df['commentText'] = df['commentText'].str.len()
#print df

#cleaning data (day 7 tutorial way)
text_clean = []
for text in df['commentText']:
    text = re.sub(r'[^a-zA-Z]',' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.rstrip()
    text_clean.append(text)
    
df['commentText'] = text_clean
df.head()
 #print 100 rows for check

# add clean text to df
df['text_clean'] = text_clean
print text_clean
print df [:100]



