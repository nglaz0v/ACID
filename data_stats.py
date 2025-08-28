"""Show some statistics based on train and test data."""

import pandas as pd

df_train = pd.read_csv("data/train-data.csv")
df_test = pd.read_csv("data/test-data.csv")

print(df_train.sample(5, random_state=42))
print(df_test.sample(5, random_state=42))
print()

print(f"{df_train.shape = }, {df_test.shape = }")
print()

print(df_train["output"].value_counts())
print(df_test["output"].value_counts())
print()

print(df_train["patient"].value_counts())
print(df_test["patient"].value_counts())
print()

patients_train = set(df_train["patient"])
patients_test = set(df_test["patient"])
print(f"patients: {len(patients_train)}, {len(patients_test)}, {len(patients_train & patients_test)}")

idx_train = df_train.drop_duplicates(["patient"]).index
idx_test = df_test.drop_duplicates(["patient"]).index
assert idx_train.shape[0] == len(patients_train)
assert idx_test.shape[0] == len(patients_test)
print()

print(df_train.loc[idx_train, "output"].value_counts())
print(df_test.loc[idx_test, "output"].value_counts())
print()

dna_rec = df_train.iloc[0]["text"].split('\n')[4]
print(dna_rec)
dna_item = dna_rec.split(' ')[0]
print(f"{len(dna_item)}: {dna_item}")
dna_seq = dna_rec.replace(' ', '').replace('.', '')
print(f"{len(dna_seq)}: {dna_seq}")
print()
