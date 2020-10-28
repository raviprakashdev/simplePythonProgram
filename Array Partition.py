class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        z = len(nums)
        sum1 = 0
        for i in range(0,z):
            if (i%2 == 0):
                sum1 += nums[i]
        return sum1
