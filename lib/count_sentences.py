#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        if (type(value) == str) and len(value) > 0:
            self._value = value
        else:
            self._value = ""
            print("The value must be a string.")
    
    def is_sentence(self):
        return self._value.endswith(".")
    
    def is_question(self):
        return self._value.endswith("?")
    
    def is_exclamation(self):
        return self._value.endswith("!")
    
    def count_sentences(self):
        new_string = self._value.replace("!", ".")
        newer_string = new_string.replace("?", ".")
        sentence_list = newer_string.split(".")
        count = 0
        for sentence in sentence_list:
            if len(sentence) > 0:
                count += 1
        return count
