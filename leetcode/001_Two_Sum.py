class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = {}
        for i , num in enumerate(nums):
            if target - num in store:
                return [store[target - num], i]
            store[num] = i
        return []
                