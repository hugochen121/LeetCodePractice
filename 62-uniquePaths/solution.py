class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if not m or not n:
            return 0
        '''

        # DP, 57%
        dp = [[1]*m for i in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # print(dp)
        return dp[-1][-1]

        '''

        # mathematical solution 97%
        # combination: m+n-2 choose m-1 to set as "down" / n-1 as "right"
        # permutation with same items: (m+n-2)!/((m-1)!(n-1)!)
        p = m+n-2
		# Taking the min of m and n minimizes the number of loops in the p choose k calculation
        k = min(m,n)-1
        total = 1
        for i in range(k):
            total*=(p-i)
        for i in range(k):
            total/=(k-i)
        return int(total)
