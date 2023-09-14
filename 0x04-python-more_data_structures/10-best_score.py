#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        score = max(a_dictionary.values())
        for key in a_dictionary:
            if a_dictionary[key] == score:
                return key
    return None
