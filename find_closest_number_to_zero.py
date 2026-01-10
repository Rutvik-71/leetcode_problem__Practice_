class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        
        for n in nums:
            if abs(n) < abs(closest):
                closest = n
            elif abs(n) == abs(closest):
                if n > closest:
                    closest = n
                    
        return closest
        
