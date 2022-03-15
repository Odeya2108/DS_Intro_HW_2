# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:00:29 2022

@author: odeya
"""

def reverse(sentence, reverse_word):
    sentence_split=sentence.split()
    index=-1
    if type(sentence)==str and type(reverse_word)==str:
        for i in sentence_split:
            index+=1
            if i == reverse_word:
                reverse_word=reverse_word[::-1]
                sentence_split[index]=reverse_word
                return " ".join(sentence_split)
        else:
            return "The word was not found" 
    else:
        print("invalid input")
print(reverse("i bla bla like banana", "bla"))
            