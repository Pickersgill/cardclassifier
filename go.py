import markov
import pandas as pd

cards = pd.read_csv("./sanitized_cards.csv", sep="|")

print(cards["r"] == 1)

model = markov.MM(cards[cards["r"] == 1][cards["g"] == 1])


for i in range(10):
    print("Card %d:\n" % i)
    new = model.generate()
    print(new)

