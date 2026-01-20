#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        first_ch = "None"
    else:
        first_ch = sentence[0]
        return (length, first_ch)