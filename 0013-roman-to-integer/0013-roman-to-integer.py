class Solution(object):
    def romanToInt(self,s):
        hashmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,
        'M':1000}
        temp = 0
        sum = 0
        i = 1
        while i < len(s):
            if hashmap[s[i]] <= hashmap[s[i-1]]:
                sum = sum + hashmap[s[i-1]]
                i += 1
            else:
                temp = hashmap[s[i]] - hashmap[s[i-1]]
                sum = sum + temp
                i += 2
        if i == len(s):
            sum = sum + hashmap[s[i-1]]
        return sum
        """
        :type s: str
        :rtype: int
        """
        