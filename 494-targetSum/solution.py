class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        
        total = sum(nums)
        if total<S or (total+S)%2:
            return 0
        total = (total+S)/2
        length = len(nums)
        '''

        # DP O(MN), 85%
        # equals to: find all possible sum(subset) == total/2
        dp = [[0]*(total+1) for i in range(length+1)]
        dp[0][0]=1  # only first index since 'zero' value is include

        for i in range(1,length+1):
            for j in range(total+1):
                if j>=nums[i-1]:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]

        # DP with memory optimize, 90%
        dp = [0]*(total+1)
        dp[0]=1 # number of combination for sum==i

        for i in range(length):
            for j in range(total, nums[i]-1, -1):
                if j>=nums[i]:
                    # sum of take num[i] or not
                    dp[j]=dp[j]+dp[j-nums[i]]
        
        return dp[-1]
        # '''
        

        #O(2^N), timeout solution
        def helper(ind, value):
            # print(ind, value)
            if ind==length:
                return 1 if value==S else 0
            
            return helper(ind+1, value+nums[ind])+helper(ind+1, value-nums[ind])
        
        
        return helper(0, 0)

