class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        e=" "
        i=len(s)-1
        while s[i]==e:
            i-=1
        for j in range(i-1,0,-1):
            if s[j]==e:
                return i-j

