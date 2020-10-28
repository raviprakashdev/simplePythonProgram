class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        result = []
        for i in nums:
            sum += i
            result.append(sum)
            
        return result
