

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        def helper(start, end):
            pre2, pre1 = 0, 0
            for i in range(start, end+1):
                cur=max(pre2+nums[i], pre1)
                pre2, pre1 = pre1, cur

            return pre1

        return max(helper(0, len(nums)-2), helper(1, len(nums)-1))    