import text_token
import pandas as pd

cards = pd.read_csv("./sanitized_cards.csv", sep="|")

corpus = []

for ind in range(cards.shape[0]):
    card = cards.iloc[ind]
    new_toks = text_token.tokenizer.tokenize(card)
    corpus += new_toks

vocab = set(corpus)
counts = {t : 0 for t in vocab}

for term in corpus:
    counts[term] = counts[term] + 1

ordered_counts = sorted(counts, key=lambda x : counts[x])

for o in ordered_counts:
    print(o, ":", counts[o])

