class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            for j in range(i):
                row[j] += row[j+1]
            row = [1] + row
        return row
            
        
