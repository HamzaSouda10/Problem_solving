class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        c=n//2
        s=0
        nums.sort()
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                s+=1
                if s>=c:
                    return nums[i]
            else:
                s=0
        return