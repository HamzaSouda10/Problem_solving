class Solution(object):
    
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c=0
        i=len(nums)-1
        while i>=0:
            if nums[i] !=val :
                c+=1
            else :
                nums.remove(nums[i])
            i-=1
        return c
    "Solution Optimale"
    
    
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for i in range (len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k

        