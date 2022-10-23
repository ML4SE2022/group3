import re

def find_surrounding_sentence(text, word):
    """
    Finds the sentence that contains the word in the text.
    """
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
    for sentence in sentences:
        if word in sentence:
            return sentence

text = "Hello, my name is John. I am a software engineer. I like to code in Python."
word = "Python"

print(find_surrounding_sentence(text, word))