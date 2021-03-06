class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
'''
        # timeout solution
        taskQ = [[s, []]]
        result=0
        
        while taskQ:
            remain, record = taskQ.pop(0)
            # print(remain, record)
            if not remain:
                result+=1
                continue

            if remain[0] != '0': 
                taskQ.append([remain[1:], record+[remain[:1]]])
            else:
                continue
            if len(remain)>1 and 0<int(remain[:2])<27:
                taskQ.append([remain[2:], record+[remain[:2]]])


        return result
'''
   
        # DP, 46%
        dp = [0]*(len(s)+1)    
        dp[0] = 1
        dp[1] = 0 if s[0]=="0" else 1
        # print(dp[:2])
        for i in range(2, len(s)+1):
            if s[i-1:i] != "0":
                dp[i]+=dp[i-1]
            if s[i-2:i-1] == "0":
                continue
            if int(s[i-2:i])<27:
                dp[i]+=dp[i-2]

        return dp[-1]