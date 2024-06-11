import pandas as pd
import os
df = pd.read_csv(os.path.join(os.path.dirname(
    __file__), '..', 'data', 'ecdict_tw.csv'))


def search(word):
    d = df[df['word'] == word]
    if len(d) > 0:
        return d.iloc[0].to_dict()
    return None
