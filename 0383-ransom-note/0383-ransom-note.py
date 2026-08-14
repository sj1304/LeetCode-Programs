class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ht = {}

        for ch in magazine:
            ht[ch] = ht.get(ch, 0) + 1

        for ch in ransomNote:
            if ch not in ht:
                return False

            if ht[ch] == 0:
                return False

            ht[ch] -= 1

        return True