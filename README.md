# Language model for detection of cancer from cfDNA

## Introduction
We present a language model ACID – Affordable Cancer Interception and Diagnostics – that can achieve high classification performance in the diagnosis of cancer exclusively from using raw cfDNA sequencing reads. We formulate ACID as an autoregressive language model. ACID is pretrained with language sentences that are obtained from concatenation of raw sequencing reads and diagnostic labels. ACID can achieve high accuracy with just 10,000 reads per sample. In summary, we present an affordable, simple yet efficient end-to-end paradigm for cancer detection using raw cfDNA sequencing reads.


## Preparation
```
pip install -r requirements.txt
gunzip data/train-data.csv.gz
gunzip data/test-data.csv.gz
```

## How to train on the example data?
### 1. Tokenizing input data
```bash
python tokenize_data.py
```

### 2. Generate a model of random weight for loading
```bash
python generate_random_weight.py
```
### 3. Training
```bash
bash train.sh
```

### Prediction
```bash
python prediction.py
```
