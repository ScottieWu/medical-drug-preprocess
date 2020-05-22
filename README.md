# Drug Name Normalization 

NHI ( National Health Insurance ) Drug preprocess and normalization.

## Flow Guide

### 1. Download open source data

```
# Download drug file from NHI website first ( Update monthly )
https://www.nhi.gov.tw/Content_List.aspx?n=238507DCFE832EAE&topn=5FE8C9FEAE863B46
Unzip and drag two txt files to data folder

# Download ATC code by running:
python -m source.ATC_code

# Download ATC alteration by running:
python -m source.ATC_alteration
```

### 2. Drug Name preprocessing

```
# Extract NHI drug data by running:
python -m preprocess.NHI_drug

# Normalize NHI drug data by running:
python -m preprocess.Extract_drug
```
