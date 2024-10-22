"""
Using the sentence class below, write a method so that you can call len on a sentence object and get the number of words in the sentence.

Hint: You might find the string method `split` useful. 
You have two attributes you might use, self._text and self._text_no_punct. Consider which should be used in your len method.
"""

import string

class Sentence:

  moods = {
    ".": "neutral",
    "!": "excited"
  }

  def __init__(self, sentence):

    punctuation = [ p for p in sentence if p in string.punctuation ]

    if not punctuation:
      raise ValueError("Sentences must contain punctuation.")
    
    final = sentence[-1]
    if final not in [".", "!"]:
      raise ValueError("Sentences must end with a punctuation mark.")

    # Store text and text without puncutation
    self._text = sentence
    self._text_no_punct = ''.join([ x for x in sentence if x not in string.punctuation ])

    # Store the sentence mood.
    self.mood = Sentence.moods[final]

  @property
  def text(self):
    # protect the text
    return self._text
  

if __name__ == "__main__":

  string_sentence = "This is a sentence."

  # This should be 4.
  my_sentence = Sentence(string_sentence)
  print(len(my_sentence))

  string_sentence = "This is a sentence ."

  # This should also be 4.
  my_sentence = Sentence(string_sentence)
  print(len(my_sentence))

