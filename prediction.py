import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
)
import datasets
import numpy as np

model_path = "opt-seq-pubmed-tokenizer"
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
ds = datasets.load_from_disk("tokenized_data")["test"]

eos_id = tokenizer.eos_token_id
pad_id = tokenizer.pad_token_id

inputs = torch.tensor(ds[0]["input_ids"]).unsqueeze(0)
gen_tokens = model.generate(
    inputs, pad_token_id=pad_id, eos_token_id=eos_id,
    do_sample=False, max_new_tokens=30).cpu()
gen_texts = tokenizer.decode(gen_tokens[0])
print(gen_texts)
