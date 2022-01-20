import markov
import pandas as pd

cards = pd.read_csv("./sanitized_cards.csv", sep="|")

def filt(card):
    return "Creature" in card["types"]

filter_index = cards[cards.apply(filt, axis=1)]

model = markov.NMM(filter_index, 2)

for i in range(10):
    print("Card %d:\n" % i)
    new = model.generate()
    print(new)

