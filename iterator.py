# This code will find out all the 're' in the given sentence
# This code will basically give demonstration about re module in python
# also this code explains the concept of iterator 

# re module is responsible for ctrl + f functionality in python
# iteartors are created using 2 most important functions
# 1) __iter__
# 2) __next__ 
# the above two functions are responsible for making the object of this code a re based iterator.



import re

class SentenceSplitter(): 

    def __init__(self, text):
         
        self.text = text

        self.words = re.findall(r'\w+', text)
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):

        if(self.index >= len(self.words)):
            raise StopIteration

        word = self.words[self.index]
        self.index += 1

        return word.upper()

sentence = SentenceSplitter("joker how are you doing and why are here?")
print('--------------------- Starting Iterator --------------------------------')

for word in sentence:
    print(word)

