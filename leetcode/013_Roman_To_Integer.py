class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = digits[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if digits[s[i]] < digits[s[i+1]]:
                sum -= digits[s[i]]
            else:
                sum += digits[s[i]]
        return sum
        