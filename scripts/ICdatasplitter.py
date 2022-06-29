#Maria Williams
#6/23/22
#script to convert csv file to a bunch of text files
#results in over 232,000 files...

import pandas as pd
import numpy as np

#prep data
data = pd.read_csv('Suicide_Detection.csv')
data_split = np.array_split(data, 3)
data = data_split[0]
data = data.drop('Unnamed: 0',axis=1)

#for each row, print the stuff from "text" into a txt file
for row in range(20200, 20210):
    fnm = data['class'][row]+str(row)+".txt"
    this = open(fnm,"w", encoding="utf-8")
    this.write(data['text'][row])
    this.close()
