class MySet:
    def __init__(self, mlist):
        self.dictionary = {};
        for item in mlist: self.dictionary.update({item: True});
    
    def add(self, val):
        self.dictionary[val] = True;

    def has(self, val):
        return val in self.dictionary;

    def delete(self, val):
        self.dictionary.pop(val);

    def size(self):
        return len(self.dictionary);
