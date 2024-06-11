import sqlite3
from dictionary.owen_2024 import get_definitions_and_pronunciations
from dictionary.ecdict_tw import search as ecdict_tw_search


def search(word):
    definition = get_definitions_and_pronunciations(word)
    zhtw_definition = ecdict_tw_search(word)
    definition['zhtw_definitions'] = zhtw_definition['translation'] if zhtw_definition else None
    return definition
