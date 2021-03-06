class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        length = len(nums)

        # DP solution O(N^2)
        dp = [1]*length # longest increasing seq before ind(i)

        for i in range(length):
            for j in range(i):
                if nums[i]>nums[j]:
                    # compare length with each LIS ending with j
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

        '''
        # timeout solution O(N^3)
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

