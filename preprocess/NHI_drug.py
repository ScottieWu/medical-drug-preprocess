import pandas as pd
import json
import re
import numpy as np
import os


with open('./data/atc_drug.json') as json_file: 
        atc_drug = json.load(json_file)
with open('./data/atc_alteration.json') as json_file: 
        atc_alteration = json.load(json_file)


files = []
for file in os.listdir("./data"):
    if file.endswith(".txt"):
        files.append('./data/' + file)

drug_file = []
for i in files:
    with open(i, encoding = 'big5', errors = 'ignore') as file:
        for k, line in enumerate(file):
            local = []
            if line[46:53].strip() == '9991231': # latest data
                local.append(line[17:27].strip())  # INSORDERID 0
                local.append(str.lower(line[54:174].strip())) # DrugName 1
                local.append(str.lower(line[236:292].strip())) # Ingredient 2
                local.append(line.split()[-1].strip()) # ATCCode 3
                if local[3] in atc_alteration.keys():
                    local[3] = atc_alteration[local[3]]
                if local[3] in atc_drug.keys():
                    local.append(str.lower(atc_drug[local[3]]))
                else:
                    local.append(np.nan)
                drug_file.append(local)

print('Done ! \n')

df = pd.DataFrame(drug_file)
df.columns = ['INSORDERID', 'DrugName', 'Ingredient', 'ATCcode', 'GenericName']
df.to_csv('./data/nhi_drug.csv', index  = False, encoding = 'big5')
