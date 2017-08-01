"""
Clean the tokenizer
"""
import os, io, glob

# set working directory
wd = 'C:\Users\zdwgh\Desktop\\tmgu_17'
os.chdir(wd)
data_path = wd

def read_txt(filepath):
    """
    read txt file form filepath and returns char content in string
    """
    f = io.open(filepath, 'r', encoding = 'utf-8')
    content = f.read()
    f.close()
    return content

def read_dir_txt(dirpath):
   # dirpath = data_path
    filenames = os.listdir(data_path)
# loop over filenames and store in list
    result_list = []
    for filename in filenames:
        filepath = data_path + filename
    # read files from filenames and store in list
        text = read_txt(filepath)
        result_list.append(text)
    # return list
    return result_list

# single text tokenization
text = read_txt('commovie.json')
print text[:100] # this prints the whole peter pan

import re

## Group text into words
# take away numbers and symbols that are not letters
tokenizer = re.compile(r'[^a-zA-Z]*') # we're creating a class including only letters
tokens = [token.lower() for token in tokenizer.split(text)] # tokens = words, .lower makes them lowercase
len(tokens) #how many words
type(tokens)

print tokens[2000:2015]


### Make it a function
def tokenize(text, lentoken = 0):
    tokenizer = re.compile(r'[^a-zA-Z]*')
    tokens = [token.lower() for token in tokenizer.split(text) 
        if len(token) > lentoken] 
    # the part after 'if' removes words that are "lentoken" characters long
    return tokens
    

print len(tokens) 


# stopword filtering
stopword = read_txt('stopword_us.txt').split()
tokens_nostop = [token for token in tokenize(text,1) if token not in stopword]
print len(tokens)
print tokens_nostop






### word counting
def tf(term, tokens):
    # raw term frequence
    result = tokens.count(term)
    return result

print tf('brexit', tokens)

lexicon = set(tokens_nostop)
tf_all = dict([(token, tokens_nostop.count(token)) for token in lexicon])

print tf_all.items()
type(tf_all)

print lexicon
print tf_all('brexit')




































