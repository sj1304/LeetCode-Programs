class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        countT = {}
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        window = {}
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("inf")
        left = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in countT and window[ch] == countT[ch]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
        