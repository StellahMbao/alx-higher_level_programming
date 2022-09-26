#!/usr/bin/python3
def multiple_returns(sentence):
    string_len = len(sentence)
    first_character = sentence[0] if string_len > 0 else None

    return (string_len, first_character)
