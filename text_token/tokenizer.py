import re
import pandas as pd

def tokenize(card):
    name = card["name"]
    shortname = name.split(",")[0]
    text = card["text"]
    retext = "{START}" + re.sub("%s|%s" % (name, shortname), "{THIS}", text) + "{END}"

    matches = re.findall(r"([0-9a-zA-Z']+)|(\{[^}]+})|([,:./])", retext)
    tokens = []
    for m in matches:
        tokens.append("".join(list(m)))
        
    return tokens
    
    

df = pd.read_csv("./sanitized_cards.csv", sep="|")

if __name__ == "__main__":
    t1 = tokenize(df.iloc[7704])
    print("_".join(t1))
    t2 = tokenize(df.iloc[10030])
    print("_".join(t2))
    t3 = tokenize(df.iloc[10333])
    print("_".join(t3))


