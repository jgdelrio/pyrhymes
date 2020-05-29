import torch
import numpy as np
from transformers import *

from config import DEFAULT_MODEL, ROOT
from utils import LOG


#          Model          | Tokenizer      | Pretrained weights shortcut
MODELS = [(GPT2LMHeadModel, GPT2Tokenizer,   'gpt2'),
          (T5Model,         T5Tokenizer,     't5-small')]


def set_seed(args):
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if args.n_gpu > 0:
        torch.cuda.manual_seed_all(args.seed)


model_class, tokenizer_class, pretrained_weights = MODELS[0]
tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
model = model_class.from_pretrained(pretrained_weights)

# Encode text
input_ids = torch.tensor(
    [tokenizer.encode("Here is some text to encode",
                      add_special_tokens=True)])  # Add special tokens takes care of adding [CLS], [SEP], <s>... tokens in the right way for each model.
with torch.no_grad():
    last_hidden_states = model(input_ids)[0]  # Models outputs are now tuples


# def retrieve_model(name=DEFAULT_MODEL):
#     model_folder = ROOT.joinpath('model', name)
#     model_folder.mkdir(parents=True, exist_ok=True)
#     if model_folder.joinpath('pytorch_model.bin').exists():
#         LOG.info(f"Model {name}: already available")
#     else:
#         try:
#             model = AlbertModel.from_pretrained(name)
#             PreTrainedModel.save_pretrained(model, model_folder)
#         except Exception as err:
#             LOG.error(f"ERROR loading the requested model {name}: {err}")
#
#     tokenizer_folder = ROOT.joinpath('model', f"{name}_tok")
#     tokenizer_folder.mkdir(parents=True, exist_ok=True)
#     if tokenizer_folder.joinpath('spiece.model').exists():
#         LOG.info(f"Tokenizer {name}: already available")
#     else:
#         try:
#             tokenizer = AlbertTokenizer.from_pretrained(name)
#             PreTrainedTokenizer.save_pretrained(tokenizer, tokenizer_folder)
#         except Exception as err:
#             LOG.error(f"ERROR loading the requested tokenizer {name}: {err}")


if __name__ == "__main__":


