class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        z = max(nums) - 1
        nums.sort()
        n = len(nums)
        y = nums[n-2] -1
        return z*y
