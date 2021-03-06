class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """

        if len(p)<2:
            return len(p)
'''
        # Time Limit Exceeded solution
        # find all continuous substrings without overlap  
        start, end = 0, 0
        substrings = set()
        for i in range(1, len(p)):
            diff = ord(p[i])-ord(p[i-1])
            if diff==1 or diff==-25:
                # end = i
                if i==len(p)-1:
                    substrings.add(p[start:i+1])
                continue
            else:
                if not(start==i-1):
                    substrings.add(p[start:i])
                start = i

        # create all possible substrings (without checking)
        candidates = set(p)

        for s in substrings:
            for i in range(2, len(s)+1):
                for j in range(0, len(s)-i+1):
                    candidates.add(s[j:j+i])

        # print(candidates)
        return len(candidates)
'''
        # 58%
        if len(p) < 2:
            return len(p)

        alphabet_cache = [0] * 26
        curr_len = 1

        # set length of first letter
        alphabet_cache[ord(p[0]) - ord('a')] = 1

        for i in range(1, len(p)):
            diff = ord(p[i]) - ord(p[i-1])
            if diff==1 or diff==-25:
                curr_len += 1
            else:
                curr_len = 1

            # the method of differentiating unique substrings is to keep track of the max number
            # of substrings that end in this specific letter i.
            ind = ord(p[i]) - ord('a')
            alphabet_cache[ind] = max(alphabet_cache[ind], curr_len)
        
        # the length of each substring is # possible substrings
        return sum(alphabet_cache)