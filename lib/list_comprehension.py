#!/usr/bin/env python3

def return_evens(num_list):
    empty_list= [num for num in num_list if num % 2 == 0]

    return empty_list

def make_exclamation(sentence_list):
    if len(sentence_list) == 0:
        return []  
    
    exclamation_list = [sentence + '!' for sentence in sentence_list]
    return exclamation_list
