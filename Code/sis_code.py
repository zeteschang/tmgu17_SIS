"""
Created on Tue Aug  1 11:41:53 2017
TMGU17_SIS
Sentiment Analysis on Youtube comments

To do list:
    - clean up data (take out NA)
    - group data into dates
    - tokenize
    - analyze sentiment
    - plot
"""


# import all modules and set working directory
import glob, os, re, nltk
import numpy as np #we load numpy as np, so we can call the library using np instead of np
import pandas as pd

wd = 'C:\Users\zdwgh\Desktop\\tmgu_17'
os.chdir(wd)



#libraries
allFiles = glob.glob('*.json')
text = pd.DataFrame() #here we initialize a Pandas DataFrame
result_list = []
for filename in allFiles:
    text = pd.read_json(filename) #since the files are in json format we use read_json. Other options include read_csv
    result_list.append(text)
    df = pd.concat(result_list)   
print df



#clean timeline
df['timestamp'] = df['timestamp'].dt.normalize()
df['month'] = df['timestamp'].dt.month
df['year'] = df['timestamp'].dt.year

df = df.set_index(['timestamp'], drop=True)



"""
#delete unused columns
df = df.drop(['date','id','hasReplies','numberOfReplies','replies','user','text_clean'], axis=1)



#calculate length of articles
df['commentText'] = df['commentText'].str.len()
print df



#Investigate cells contains specific word(s)
df[df["tokens"].str.contains("propaganda")] #result 278 comments
df[df["text_clean"].str.contains("immigrants")] #result 84

"""


#clean data
text_clean = []
for text in df['commentText']:
    text = re.sub(r'[^a-zA-Z]',' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.rstrip()
    text_clean.append(text)
df['text_clean'] = text_clean



#tokenization
tokens = []
for i in range(len(df)):
    tokens.append(df['text_clean'][i].lower().split())
df['tokens'] = tokens



#clean token with nltp   nosw=nostopwords
from nltk.corpus import stopwords
stop = stopwords.words('english')
 
tokens_nosw=[]  
for doc in tokens:
    doc_nosw = [w for w in doc if w not in stop]
    tokens_nosw.append(doc_nosw)
df['doc_nosw'] = tokens_nosw



"""
#word frenquency count
from nltk.probability import *
fd = FreqDist(tokens_nosw)
"""



#sentimental analysis
labmt = pd.read_csv('res\labmt_dict.csv', sep = '\t', encoding = 'utf-8', index_col = 0)
avg = labmt.happiness_average.mean()
sent_dict = (labmt.happiness_average - avg).to_dict()

sent_vects = []
for s in tokens:
    sent_vects.append(sum([sent_dict.get(token,0.0) for token in s]))
df['sentiment'] = sent_vects



#plot
import seaborn as sns
import timeit
df = df.pivot_table(index='month', columns='year', values='sentiment', aggfunc=np.median)
sns.heatmap(df, annot=True, fmt=".1f")


















