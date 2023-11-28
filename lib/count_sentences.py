#!/usr/bin/env python3
class MyString:
    def _init_(self, value=''):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        if not isinstance(self.value, str):
            raise AssertionError("The value must be a string.")
        
        punctuations = ['.', '!', '?']
        modified_str = self.value.replace('!!', '.').replace('?', '.').replace('!', '.')
        sentences = [sentence for sentence in modified_str.split('.') if sentence.strip()]
        return len(sentences)