import os
import pandas as pd
from thefuzz import process

# Change directory
os.chdir(r"/Users/khantnaing/Documents/VSCode/SDP/ndcxls")

# Import the NDC dataset
filename = "product.csv"
dataset = pd.read_csv(filename)

# Find the closest match
query = "Metformin"
extract = process.extractOne(query, dataset["PROPRIETARYNAME"])
print(dataset.iloc[extract[2]])

