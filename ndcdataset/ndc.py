import os
import pandas as pd
from thefuzz import process

# Change directory
os.chdir(r"/Users/khantnaing/Documents/VSCode/SDP/ndcxls")

# Import the NDC dataset
filename = "product.csv"
dataset = pd.read_csv(filename)

queries = ['Tylneol', 'MOUTH EVERYO', 'CHRISTOPHER HO', 'ATORVASTATIN', 'TAKE1TABLETE', '0349518-178', 'N.M.D.RPi Hat', 'Y30', 'Walgreeks', 'Mtouirot', '(413)527-0777', '2024-03-09 15:32 (EST'] 

threshold = 85

med_list = []
for query in queries:
  extract = process.extractOne(query, dataset["PROPRIETARYNAME"], score_cutoff=threshold)
  if extract:
    med_list.append(extract[0])
print(med_list)