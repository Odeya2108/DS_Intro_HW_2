# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:00:29 2022

@author: odeya
"""

def reverse(sentence, reverse_word):
    split_sentence=sentence.split()
    index=-1
    if type(sentence)==str and type(reverse_word)==str:
        for i in split_sentence:
            index+=1
            if i == reverse_word:
                reverse_word=reverse_word[::-1]
                split_sentence[index]=reverse_word
                return " ".join(split_sentence)
        else:
            return "The word was not found" 
    else:
        print("invalid input")
print(reverse("I like apples and I also like bananas", "like"))
            
