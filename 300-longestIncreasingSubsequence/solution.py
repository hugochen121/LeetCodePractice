import sys
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        length = len(nums)
        dp = [0]*length

        for i in range(length):
            best = 1
            for j in range(i):
                if nums[i]>nums[j]:
                    # compare length with each LIS ending with j
                    best = max(best, dp[j]+1)

            dp[i] = best

        return max(dp)    

        '''
        # timeout solution
        cands = []
        ind = 0
        
        while ind <length:
            for i in range(len(cands)):
                
                if cands[i][-1]<nums[ind]:
                    cands.append(cands[i]+[nums[ind]]) 
            cands.append([nums[ind]])        
            ind+=1
        # print(cands)    
        
        best = 1
        
        for c in cands:
            best = len(c) if len(c)>best else best

        return best
        '''

        