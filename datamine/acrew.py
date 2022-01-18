import re
import json
import time
import datetime
import pandas as pd

with open("./AtomicCards.json") as card_data:
    j_data = json.load(card_data)
    meta_data = j_data["meta"]
    data = j_data["data"]
    keys = list(data.keys())

with open("./SetList.json") as set_data:
    set_j_data = json.load(set_data)
    set_meta_data = set_j_data["meta"]
    set_data = set_j_data["data"]
    dated = { time.mktime(datetime.datetime.strptime(s["releaseDate"], "%Y-%m-%d").timetuple()) \
        : (s["code"] if "parentCode" not in s.keys() else s["parentCode"], s["releaseDate"]) for s in set_data}
    date_list = list(dated.keys())
    date_list.sort()
    sorted_dated = [dated[x] for x in date_list]

INVALID_SETS = ["PCEL", "PRM"]
FORBIDDEN_SETS = ["UST", "UNH", "UGL", "UND", "AFR", "PCEL"]

def has_forb_set(c):
    ps = c["printings"]
    if len(list(filter(lambda x : x not in FORBIDDEN_SETS, ps))) == 0:
        return True
    return False

FORBIDDEN_TYPES = ["Dungeon"]

def has_forb_type(c):
    if c["type"] in FORBIDDEN_TYPES:
        return True
    return False

double_face_re = re.compile(r"(.+) // (.+)")

def get_print(c):
    valid_printings = list(filter(lambda x : len(x) <= 3 and x not in INVALID_SETS, c["printings"]))
    for i in range(len(sorted_dated)):
        c_set = sorted_dated[i]
        if c_set[0] in valid_printings:
            return(c_set)

# remove UN-sets
# remove Dungeon type
# check two-face

rows = []
ignore_count = 0

for key in keys:
    for d in data[key]:
        if not(has_forb_type(d)) and not(has_forb_set(d)):
            if "side" in d.keys():
                m = double_face_re.match(d["name"])
                if m:
                    name = m.group(1) if d["side"] == "a" else m.group(2)
                else:
                    name = d["name"]
            else:
                name = d["name"]
            
            printing = get_print(d)
            if printing:
                colours = d["colors"]
                red = "R" in colours
                green = "G" in colours
                black = "B" in colours
                white = "W" in colours
                blue = "U" in colours
        
                #print("Name: %s\nFirst Printing: %s\nR: %s\nG: %s\nB: %s\nW: %s\nU: %s" % \
                #    (name, printing[1], red, green, black, white, blue))
                rows.append({
                    "name" : name,
                    "printed" : printing[1],
                    "r" : int(red),
                    "g" : int(green),
                    "b" : int(black),
                    "w" : int(white),
                    "u" : int(blue)
                })
            else:
                print("Row ignored")


dataframe = pd.DataFrame(rows, columns=["name", "printed", "r", "g", "b", "w", "u"])
dataframe.to_csv("sanitized_cards.csv", sep="|")

