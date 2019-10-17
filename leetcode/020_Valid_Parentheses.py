class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = [None]
        pdict = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in pdict:
                if pdict[i] != p.pop():
                    return False
            else:
                p.append(i)
        return len(p) == 1