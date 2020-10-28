class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """ 
        f0,f1 = cost[0],cost[1]
        for i in range(2,len(cost)):
            tmp = cost[i] + min(f0,f1)
            f0 = f1
            f1 = tmp
        return min(f0,f1)
        
            
