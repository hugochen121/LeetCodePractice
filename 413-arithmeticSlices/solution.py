class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A)<3:
            return 0
        '''
        # naive solution
        diff = [None]*len(A)
        for i in range(1, len(A)):
            diff[i] = A[i] - A[i-1]
        # print(diff)
        records = dict()

        temp=None
        counter=1
        for i in range(1, len(diff)):
            if temp == diff[i]:
                counter+=1
            else:
                if not temp in records:
                    records[temp]=[counter]
                else:
                    records[temp].append(counter)
                
                temp = diff[i]
                counter = 1

        if not temp in records:
            records[temp]=[counter]
        else:
            records[temp].append(counter)
                
        # print(records)

        result=0
        for k, v in records.items():
            for vv in v:
                if vv>1:
                    result+= ((vv-1)+1)*(vv-1)/2

        return result
        '''

        # dp solution
        dp = [0]*len(A)
        for i in range(2, len(A)):
            # each 3 make a 3-slice, length+1 == a new 3-slice & a length+1-slice
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1

        return sum(dp)