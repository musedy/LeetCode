class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        prefix = min(strs, key = len)
        for i, j in enumerate(prefix):
            for word in strs:
                if word[i] != j:
                    return prefix[:i]
        return 