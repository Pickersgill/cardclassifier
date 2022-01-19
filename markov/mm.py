import text_token
import pandas as pd
import numpy as np
import random
import sys

class MM:
    def __init__(self, cards):

        self.bigrams = []
        self.vocab = set()    

        print("Building new model...")

        nrows = cards.shape[0]
        print("Found data for %d cards.\nGenerating bigrams...\n" % nrows)

        
        for ind in range(nrows):

            complete = int((ind + 1) / nrows * 100)
            sys.stdout.write("█" * complete)
            sys.stdout.write("\b" * complete)
            sys.stdout.flush()

            card = cards.iloc[ind]

            new_toks = text_token.tokenizer.tokenize(card)
            new_bigrams = [(new_toks[k-1], new_toks[k]) for k in range(1, len(new_toks))]

            self.vocab = self.vocab.union(set(new_toks))
            self.bigrams += new_bigrams

    
        print()
        print("Calculating transition matrix...\n")
        self.vocab_map = {v[1] : v[0] for v in enumerate(self.vocab)}
        self.reverse_vocab_map = {b : a for a, b in self.vocab_map.items()}

        M = np.zeros((len(self.vocab_map), len(self.vocab_map)), dtype=np.longdouble)
        B = len(self.bigrams)

        for i, b in enumerate(self.bigrams):
            complete = int((i + 1) / B * 100)
            sys.stdout.write("█" * complete)
            sys.stdout.write("\b" * complete)
            sys.stdout.flush()

            head = b[0]
            tail = b[1]
            i = self.vocab_map[head]
            j = self.vocab_map[tail]
            M[i][j] += 1    
        
        print()
        print("Normalizing matrix...")

        # NEED TO MATRIXIFY
        rows = M.shape[0]
        for i in range(rows):

            complete = int((i + 1) / rows * 100)
            sys.stdout.write("█" * complete)
            sys.stdout.write("\b" * complete)
            sys.stdout.flush()

            row = M[i]
            fac = 1
            if row.sum() != 0:
                fac = 1 / row.sum()
                
            for j in range(len(row)):
                M[i][j] *= fac

            
        self.trans_matrix = M
        print()
        print("Model complete...\n")

    def generate(self):
        i = self.vocab_map["{START}"]
        end_state = self.vocab_map["{END}"]

        construct = "{START} "
        v_size = len(self.vocab)

        while i != end_state:
            j = random.choices(range(0, v_size), weights=self.trans_matrix[i], k=1)[0]
            next_tok = self.reverse_vocab_map[j]
            construct += next_tok + " "
            i = j
        
        return construct
        



