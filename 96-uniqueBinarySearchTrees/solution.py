class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        if not n:
            return 0

        if n<3:
            return n

        # DP solution O(N^2), record numTree of value(i).
        # memorize the numCombination of subtrees(sub-problem), then get total count
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                # print(i, j, i-j-1)
                dp[i]+=dp[j]*dp[i-j-1]

        return dp[-1]