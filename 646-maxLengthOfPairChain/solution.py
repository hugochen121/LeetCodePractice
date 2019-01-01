import sys
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        
        if not pairs:
            return 0
        if len(pairs)<2:
            return 1

        
        
        '''
        # greedy, 32%
        pairs = sorted(pairs ,key=lambda l:l[1])
        visit = set() 
        visit.add(tuple(pairs[0]))
        # print(pairs)
        
        flag = True 
        pre, cur = pairs[0], None

        while flag:
            flag = False
            cur=None
            for p in pairs:
                if tuple(p) in visit:
                    continue
                # print(pre, cur, p)

                if not cur and p[0]>pre[1]:
                    cur = p
                if p[0]>pre[1] and (p[1]<=cur[1]):
                    cur = p
                    flag = True
            
            if flag: 
                pre = cur
                visit.add(tuple(cur))

        print(visit)
        return len(visit)
        '''

        # DP, timeout
        pairs = sorted(pairs ,key=lambda l:l[0])
        print(pairs)
        length = len(pairs)
        dp=[1]*length
        for i in range(1, length):
            
            for j in range(i):
                if pairs[i][1]<pairs[j][0]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
