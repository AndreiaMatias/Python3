# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:35:13 2020

@author: deiamat
"""
 
"""This program uses ceasar cypher to encode a message."""
sentence = "the cat sat on the mat"
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def decypher(text, n):
    new_text=""
    for char in text:
        if char in letters:
            if letters.index(char)+n < 26:
                new_text+=letters[letters.index(char)+n]
            else:
                new_text+=letters[letters.index(char)+n-26]
        else:
            new_text+=char
    return new_text

new_sentence = decipher(sentence,3)


def undecypher(text, n):
    new_text=""
    for char in text:
        if char in letters:
            if letters.index(char)-n < 26:
                new_text+=letters[letters.index(char)-n]
            else:
                new_text+=letters[letters.index(char)-n-26]
        else:
            new_text+=char
    return new_text


old_sentence = undecipher(new_sentence, 3)