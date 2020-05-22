import pandas as pd
import numpy as np
import json
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from preprocess.utils import clean_text, lemmatize, important

drug = pd.read_csv('./data/nhi_drug.csv', encoding = 'big5')

drug['Ingredient'] = drug['Ingredient'].apply(lambda x : lemmatize(x))
drug['DrugExtract'] = drug['DrugName'].apply(lambda x : clean_text(x))

bow = []
for i in list(drug['DrugExtract']):
    for j in i.split():
        bow.append(j)

N = len(bow)
idf = np.log(N/pd.Series(bow).value_counts()).to_dict()


drug['DrugExtract'] = drug['DrugExtract'].apply(lambda x : important(x, idf, 6))


drug = drug[['INSORDERID', 'DrugName', 'DrugExtract', 'Ingredient', 'ATCcode', 'GenericName']]

print('Done ! \n')

drug.to_csv('./data/drug.csv', index  = False, encoding = 'big5')

# ID = {
# 'AC33023100',
# 'AC34348100',
# 'A028947212',
# 'A043869277',
# 'AC412691G0',
# 'AC412701G0',
# 'A018062100',
# 'AA58181100',
# 'AB58181100',
# 'AC58181100',
# 'AC59884157',
# 'AC303091G0',
# }

# print(drug.loc[[i for i, k in enumerate(list(drug['INSORDERID'])) if k in ID]])














