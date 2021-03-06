class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result=[]
        if not nums:
            return result
        
        # DFS 35%
        visit=set()
        def helper(visit, perms):
            # print(remain, perms)
            if len(visit)==len(nums):
                result.append(perms)
                return
            
            for i in range(len(nums)):
                if not(i in visit):
                    visit.add(i)
                    helper(visit, perms+[nums[i]])
                    visit.remove(i)
    
        helper(visit, [])
        return result
        '''
        # BFS 30%
        taskQ=[[nums, []]]
        while taskQ:
            remain, perm = taskQ.pop(0)
            if not remain:
                result.append(perm)
            for i in range(len(remain)):
                taskQ.append([remain[:i]+remain[i+1:], perm+[remain[i]]])

        return result
        '''    
    
        