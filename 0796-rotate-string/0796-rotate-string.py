class Solution(object):
    def rotateString(self, s, goal):

        if len(s) != len(goal):
            return False

        n = len(s)

        for start in range(n):

            if s[start] != goal[0]:
                continue

            match = True

            for i in range(n):
                if s[(start + i) % n] != goal[i]:
                    match = False
                    break

            if match:
                return True

        return False