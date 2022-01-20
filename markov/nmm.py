import text_token
import pandas as pd
import numpy as np
import random
import sys

class TwoMM:
    def __init__(self, cards, memory=2):

        self.memory = memory
        self.grams = []
        self.vocab = set()
        self.openings = []

        print("Building new model...")

        nrows = cards.shape[0]
        print("Found data for %d cards.\nGenerating Ngrams...\n" % nrows)

        
        for ind in range(nrows):

            complete = int((ind + 1) / nrows * 100)
            sys.stdout.write("█" * complete)
            sys.stdout.write("\b" * complete)
            sys.stdout.flush()

            card = cards.iloc[ind]

            new_toks = text_token.tokenizer.tokenize(card)
            self.openings.append(new_toks[0:memory])
            new_grams = [tuple(new_toks[k-(memory+1):k]) for k in range(memory+1, len(new_toks) + 1)]

            self.vocab = self.vocab.union(set(new_toks))
            self.grams += new_grams

    
        print()
        print("Calculating transition matrix...\n")
        self.vocab_map = {v[1] : v[0] for v in enumerate(self.vocab)}
        self.reverse_vocab_map = {b : a for a, b in self.vocab_map.items()}

        M = np.zeros([len(self.vocab_map)] * (self.memory + 1), dtype=np.short)
        print(M.shape)
        B = len(self.grams)

        for i, gram in enumerate(self.grams):
            complete = int((i + 1) / B * 100)
            sys.stdout.write("█" * complete)
            sys.stdout.write("\b" * complete)
            sys.stdout.flush()

            inds = []

            for term in gram:
                inds += [self.vocab_map[term]]
            inds = tuple(inds)
            M[inds] += 1
        
        print()
        self.trans_matrix = M
        print()
        print("Model complete...\n")
    
    def vocab_to_num(self, terms):
        return list(map(lambda x : self.vocab_map[x], terms))

    def num_to_vocab(self, nums):
        return list(map(lambda x : self.reverse_vocab_map[x], nums))

    def generate(self):
        start = random.choice(self.openings)
        end_state = self.vocab_map["{END}"]
        history = self.vocab_to_num(start)

        count=0
    
        while history[-1] != end_state:
            inds = tuple(history[-self.memory:])
            probs = self.trans_matrix[inds]
            if probs.sum() == 0:
                n = end_state
            else:
                n = random.choices(range(0, probs.shape[0]), weights=probs, k=1)[0]
            history.append(n)

        construct = " ".join(self.num_to_vocab(history))
        
        return construct
        



