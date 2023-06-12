#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        s = len(sentence)
        first = sentence[0]
        return (s, first)
    return (0, None)
