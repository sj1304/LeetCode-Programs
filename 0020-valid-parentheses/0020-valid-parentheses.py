class Solution(object):
    def isValid(self, s):
        st = []
        match = {'(': ')', '[': ']', '{': '}'}

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                st.append(s[i])
            else:
                if len(st) == 0:
                    return False

                temp = st.pop()
                if match[temp] != s[i]:
                    return False

        if(len(st)!=0):
            return False
        else:
            return True