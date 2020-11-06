from Node import Node
from string import ascii_lowercase

# Faster to use a set as it is O(1) time to check if it contains a word
# valid_words = set()

class WordGameNode(Node):
    def __init__(self, name, parent = None):
        # Ensure lowercase letters (no digits or special chars)
        for letter in name:
            assert letter in ascii_lowercase
        
        self.name = name
        self.parent = parent

    def __str__(self):
        return self.name

    def get_children(self):
        # all one letter mutations of the word
        child_words = []
        name = self.name

        for i in range(len(name)):
            for letter in ascii_lowercase:
                child_words.append(name[:i] + letter + name[i+1:])
                #append all variations to child words
        
        # remove original names using a list comprehension
        children = [n for n in child_words if n != name]
        # return all valid child words
        return [WordGameNode(child, self) for child in children if child in valid_words]

    def get_parent(self):
       return self.parent

    def get_path(self):
        path = [self]
        while self.get_parent() != None:
            path.append(self.parent)
            self = self.get_parent()
        return path

#######################################
def read_dictionary(filename, length):
    global valid_words 
    valid_words = set()
    
    with open(filename) as f:
        for line in f:
            word = line.strip()
            if is_valid(word) and length == len(word):
                valid_words.add(word.strip())

def is_valid(word):
    return word.islower() and word.isalpha()
