class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past={}
        for i,v in enumerate(nums):
            comp = target - v
            if comp in past:
                return [past[comp], i]
            past[v]=i
        
