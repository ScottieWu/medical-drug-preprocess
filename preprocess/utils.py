from nltk.stem import WordNetLemmatizer
import numpy as np
lemmatizer = WordNetLemmatizer() 

luxury = {
'mg', 
'ml',
'gm',
'mcg',
'units', 
'unit', 
'vial', 
'vials', 
'in', 
'for', 
'plus',
'suportory',
'suppository',
'injection',
'tablet',
'capsule',
'solution',
'and'
}

def clean_text(x):
    try:
        eval(x)
        x = x[1:-1]
    except:
        pass
    if x.count('"') == 1:
        index = x.find('"')
        x = x[:index] + x[index+1:]
    replacement = {'(': ' (', ')': ') ', '（': ' （', '）': '） ', ',': ' ,', '治': ' 治'}
    for r, l in replacement.items():
        x = x.replace(r, l)
    res = [ lemmatizer.lemmatize(y) for y in x.split()]
    ct, index = [], []
    for i, k in enumerate(res):
        if len(k) >= 2 and k not in luxury:
            delete = 0
            for j in '"/)(（）％%':
                if j in k:
                    delete += 1
                    break
            for l in '0123456789':
                if (l in k and 'mg' in k) or (l in k and 'ml' in k) or (l in k and 'gm' in k) or (l in k and 'mcg' in k) or (l in k and 'iu' in k) or (l in k and '.' in k) or k.isnumeric():
                    delete += 1
                    break
            if len(k) >= 2 and delete == 0:
                ct.append(k)
                index.append(i)
    if len(ct) == 0:
        return ' '.join(res)
    else:
        return ' '.join(ct)

def lemmatize(x):
    x = str(x).split()
    return ' '.join([lemmatizer.lemmatize(y) for y in x])


def important(x, idf, threshold):
    x = x.split()
    index = [i for i, y in enumerate(x) if idf[y] >= threshold]
    res = []
    for i, k in enumerate(index):
        if i == k:
            res.append(x[i])
        else:
            break
    if len(res) == 0:
        score = np.array([idf[y] for y in x])
        res.append(x[np.argmax(score)])

    return ' '.join(res)
