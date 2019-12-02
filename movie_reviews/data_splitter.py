#All the necessary imports
import numpy as np
import nltk
import pandas as pd
import os
import re
import csv
import gzip

#this

directory = "./aclImdb" 
for i in ["train", "test"]:
    labeledData[i] = []
    for sentiment in ["pos", "neg"]:
        score = 1 if sentiment == "pos" else 0
        path = os.path.join(directory, i, sentiment)
        for filename in os.listdir(path):
            with open(os.path.join(path, filename), encoding="utf8") as f:
                labeledData[i].append([f.read(), score])  #Initially adds them to separate lists

np.random.shuffle(labeledData["train"]) #Shuffling
labeledData["train"] = pd.DataFrame(labeledData["train"], columns = ['text', 'sentiment']) #Putting them in a dataframe
np.random.shuffle(labeledData["test"])
labeledData["test"] = pd.DataFrame(labeledData["test"], columns = ['text', 'sentiment'])
labeledData["train"], labeledData["test"] #Prints out both pandas dataframes


train1 = labeledData["train"].iloc[:6250].to_csv (r'C:\Users\mdodda3-gtri\Untitled Folder\train1.csv.gz', index = None, header=False, compression='gzip')
train2 = labeledData["train"].iloc[6250:12500].to_csv (r'C:\Users\mdodda3-gtri\Untitled Folder\train2.csv.gz', index = None, header=False, compression='gzip')
train3 = labeledData["train"].iloc[12500:18750].to_csv (r'C:\Users\mdodda3-gtri\Untitled Folder\train3.csv.gz', index = None, header=False, compression='gzip')
train4 = labeledData["train"].iloc[18750:].to_csv (r'C:\Users\mdodda3-gtri\Untitled Folder\train4.csv.gz', index = None, header=False, compression='gzip')

test1 = labeledData["test"].iloc[:6250].to_csv (r'C:\Users\mdodda3-gtri\Untitled Folder\test1.csv.gz', index = None, header=False, compression='gzip')
test2 = labeledData["test"].iloc[6250:12500].to_csv (r'C:\Users\mdodda3-gtri\Untitled Folder\test2.csv.gz', index = None, header=False, compression='gzip')
test3 = labeledData["test"].iloc[12500:18750].to_csv (r'C:\Users\mdodda3-gtri\Untitled Folder\test3.csv.gz', index = None, header=False, compression='gzip')
test4 = labeledData["test"].iloc[18750:].to_csv (r'C:\Users\mdodda3-gtri\Untitled Folder\test4.csv.gz', index = None, header=False, compression='gzip')
