#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        first_ch = (0, None)
    else:
        return (length, sentence[0])
