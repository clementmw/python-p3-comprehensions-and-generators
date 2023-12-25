#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [i for i in num_list  if i%2 == 0 ]
    return even_list
num_list = [0,1,3,5,7,8,9]
result = return_evens(num_list)
print(result)

    

def make_exclamation(sentence_list):
    exclamation = [i + "!" for i in sentence_list]
    return exclamation
sentence_list = ["Hello", "I'm doing great", "Python is fun"]
result = make_exclamation(sentence_list)
print(result)