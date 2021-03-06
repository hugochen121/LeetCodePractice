class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        length = len(nums)

        '''
        # brute force O(N^2), timeout
        cand=[]
        for i in range(len(nums)):
            temp = nums[i]
            cand.append(temp)

            for j in range(i+1, len(nums)):
                temp+=nums[j]
                cand.append(temp)

        return max(cand)

        # DP solution, keep track of currentSum O(N), 70%
        dp = [0]*length
        dp[0] = nums[0]
        for i in range(1, length):
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        # print(dp)
        return max(dp)
        '''

        # DP solution, keep only latest values O(N), 54%
        curr = nums[0]
        best = nums[0]
        for i in range(1, length):
            curr = max(curr+nums[i], nums[i])
            best = max(best, curr)

        return best