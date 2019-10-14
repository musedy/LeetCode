class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        str_x = str(x)
        r = int(len(str_x)/2)
        for i in range(r):
            if str_x[i] != str_x[-i-1]:
                return False
        return True
        