class Solution(object):
    def removeAnagrams(self, words):
        def sortWord(w):
            return ''.join(sorted(w))
        
        i = 1
        while i < len(words):
            if sortWord(words[i]) == sortWord(words[i - 1]):
                words.pop(i)  # remove the current word
            else:
                i += 1  # only move ahead if no removal
        return words