class Solution(object):
    def maxFreqSum(self, s):
        vhashmap={}
        chashmap={}
        for i in range(len(s)):
            if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' 
            or s[i]=='u'):
                vhashmap[s[i]]=vhashmap.get(s[i],0)+1
            else:
                chashmap[s[i]]=chashmap.get(s[i],0)+1
        vmax=max(vhashmap.values()) if vhashmap else 0
        cmax=max(chashmap.values()) if chashmap else 0
        return (vmax+cmax)
            

                
        """
        :type s: str
        :rtype: int
        """
        