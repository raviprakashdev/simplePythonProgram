class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        a,b = 0,1
        for i in range(N):
            a,b = b,b+a            
        return a
