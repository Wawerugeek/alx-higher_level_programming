#!/usr/bin/python3
def multiple_returns(sentence):
    my = ()
    if len(sentence) == 0:
        my =0, "None"
    else:
        my = len(sentence), sentence[0]
    return my
