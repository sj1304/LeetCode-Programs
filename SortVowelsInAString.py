class Solution(object):
    def sortVowels(self,s):
        vowels = "AEIOUaeiou"
        extracted = [ch for ch in s if ch in vowels]
        extracted.sort()    
        result = []
        idx = 0
        for ch in s:
            if ch in vowels:
                result.append(extracted[idx])
                idx += 1
            else:
                result.append(ch)
        return "".join(result)




                
            
        