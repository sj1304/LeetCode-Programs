class Solution(object):
    def doesAliceWin(self,s):
        vowels = set("aeiou")
        cnt = sum(1 for ch in s if ch in vowels)
        return cnt > 0  

 
        
        