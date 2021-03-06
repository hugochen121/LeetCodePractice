import math
class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        
        if not piles:
            return 0

        # O(max(piles)*log(P)), 60%
        left, right = 0, max(piles)
        best = right
        while left < right:
            mid = left+(right-left)//2
            if not mid: break
            hours = 0
            # print(mid, left, right)    
            for p in piles:
                '''
                hours += math.ceil(p/mid)   #time-consuming 10%
                '''
                if p%mid:
                    hours += p//mid+1
                else:
                    hours += p//mid
            if H>=hours and mid<best:
                best = mid
            if hours>H:
                left = mid+1
            else:
                right = mid  

        return best                   


