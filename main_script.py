from os.path import dirname, join
import numpy as np
import pandas as pd


dirname = dirname(__file__)
filename = join(dirname, 'subjects.txt')
with open(filename , 'r') as f:
    subjects = f.readlines()
for i in range(0, len(subjects)):
    subjects[i] = int(subjects[i].rstrip())

main_df = pd.DataFrame()
subjects = []
y661