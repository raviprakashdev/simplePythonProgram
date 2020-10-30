class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        for i in range(len(s)):
            s[i]=s[i][::-1]
        return " ".join(s)
        
