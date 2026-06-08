class Solution(object):
    def myAtoi(self, s):
        newn = ""
        ifstart = 0

        for i in s:
            if i == " " and ifstart == 0:
                continue
            elif (i == "-" or i == "+") and ifstart == 0:
                newn += i
                ifstart = 1
            elif i.isdigit():
                newn += i
                ifstart = 1
            else:
                break

        if newn == "" or newn == "+" or newn == "-":
            return 0

        num = int(newn)
        if num < -2147483648:
            return -2147483648
        if num > 2147483647:
            return 2147483647

        return num
